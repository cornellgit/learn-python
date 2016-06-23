import threading
import time


# threads for I/O bound problems
# Use processes for CPU-bound problems
# 1. thread as function
def print_thread(num):
    time.sleep(1)
    print("%s: %s" % (threading.current_thread(), num))


# start 10 thread
for i in range(10):
    t = threading.Thread(target=print_thread, args=(i,))
    t.start()


# 2. thread as a subclass, it helps thread to encapsulate states also
class PrintThread(threading.Thread):
    def __init__(self, num):
        threading.Thread.__init__(self)
        self.num = num

    def run(self):
        time.sleep(1)
        print("%s: %s" % (threading.current_thread(), self.num))


for i in range(10):
    t = PrintThread(i)
    t.start()
