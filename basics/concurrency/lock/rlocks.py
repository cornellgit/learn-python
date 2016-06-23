import threading


# reentrant lock can be relaesed by the same thread
# e.g. use it to create a synchronized data structure

# a synchronized counter
class Counter:
    def __init__(self):
        self.cnt = 0
        self.lock = threading.RLock()

    def inc(self):
        with self.lock:
            self.cnt += 1

    def dec(self):
        with self.lock:
            self.cnt -= 1


def adder(c):
    for i in range(10000):
        c.inc()


def decer(c):
    for i in range(10000):
        c.dec()


c = Counter()
t1 = threading.Thread(target=adder, args=(c,))
t2 = threading.Thread(target=decer, args=(c,))

t1.start()
t2.start()

t1.join()
t2.join()

assert c.cnt == 0
