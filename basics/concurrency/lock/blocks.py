# requires all of the processes to reach it before any of them proceeds.
import random
import time
from multiprocessing import Barrier, Process
from os import getpid as pid


# start two process and wait for random time, then execute code after barrier simultaneously
# pay attention to awake time
def print_time(barrier):
    sleep = random.randint(1, 3)
    print(pid(), "Sleep", sleep)
    time.sleep(sleep)

    # blocks until  all the threads called this function, they are all released simultaneously
    # i is between 0 to n-1
    i = barrier.wait()
    print(pid(), "Awake", time.time())
    # only one process will print this
    if i == 0:
        print(pid(), 'Passed Barrier')


b = Barrier(2)
p_list = [Process(target=print_time, args=(b,)),
          Process(target=print_time, args=(b,))]

for p in p_list:
    p.start()

for p in p_list:
    p.join()
