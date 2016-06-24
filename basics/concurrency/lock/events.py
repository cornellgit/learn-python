import random
import time
from threading import Thread, Event, current_thread


def worker(e):
    print(current_thread(), 'start')
    time.sleep(random.randint(1, 5))
    print(current_thread(), 'end')
    e.set()
    # set flag true, all threads waiting for it to become true are awakened.


events = []
for i in range(3):
    events.append(Event())
    t = Thread(target=worker, args=(events[-1],))
    t.start()

for e in events:
    #  wait() method blocks until the flag is true
    e.wait()
    e.clear()
    # reset flag false. Subsequently, threads calling wait() will block

print('ALL EVENTS PROCESSED')
