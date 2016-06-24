# condition identifies a change of state
# 1. thread A waits for a specific condition
# 2. thread B notify this condition has taken place
# 3. thread A acquires the lock to get exclusive access to the shared resource.

# example, synchronized buffer with max size 10
# two fast producer, one slow consumer

import time
from threading import Condition, Thread, current_thread

buf = []
condition = Condition()


class Consumer(Thread):
    def __init__(self):
        Thread.__init__(self)

    def consume(self):
        global buf
        global condition

        with condition:
            if len(buf) == 0:
                # wait releases the lock, and then blocks until another thread awakens it by calling notify()
                print('c-%s: NOTHING TO CONSUME' % (current_thread(),))
                condition.wait()
            print('c-%s: size(%s)' % (current_thread(), len(buf)))
            buf.pop()
            # notify the producer buffer is not full
            condition.notify()

    def run(self):
        for i in range(41):
            self.consume()
            time.sleep(1)


class Producer(Thread):
    def __init__(self):
        Thread.__init__(self)

    def produce(self):
        global buf
        global condition

        with condition:
            if len(buf) == 10:
                condition.wait()
                print('p-%s: BUFFER FULL' % (current_thread(),))
            buf.append(1)
            print('p-%s: size(%s)' % (current_thread(), len(buf)))
            # notify() and notify_all() methods don’t release the lock
            # notify wake up one thread waiting on this condition, that it can consume
            condition.notify()

    def run(self):
        for i in range(20):
            self.produce()
            time.sleep(1)


threads = [Producer(), Producer(), Consumer()]
for t in threads:
    t.start()
for t in threads:
    t.join()
