import threading
import time

loc = threading.Lock()
global_counter = 0


# notice that any thread can release the lock
def increment():
    global global_counter
    with loc:
        print("INCREASING...")
        for i in range(10):
            global_counter += 1
            print(global_counter)
            time.sleep(1)


def decrement():
    global global_counter
    with loc:
        print("DECREASING...")
        for i in range(10):
            global_counter -= 1
            print(global_counter)


threads = (threading.Thread(target=increment),
           threading.Thread(target=decrement))

# notice that increment is ahead if decrement
for t in threads:
    t.start()

for t in threads:
    t.join()
