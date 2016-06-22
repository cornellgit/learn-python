import threading
import time


# threads for I/O bound problems
# Use processes for CPU-bound problems
def print_thread(num):
    time.sleep(1)
    print("%s: %s" % (threading.current_thread(), num))


# start 10 thread
for i in range(10):
    t = threading.Thread(target=print_thread, args=(i,))
    t.start()
