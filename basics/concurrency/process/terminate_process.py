import multiprocessing
import os
import time


# termination and delay
def do_it_n_sleep():
    for i in range(1000):
        time.sleep(1)
        print('pid: %s param: %s' % (os.getpid(), i))


p = multiprocessing.Process(target=do_it_n_sleep)
print('pid: %s param: %s' % (os.getpid(), 'main'))

p.start()
time.sleep(6)
p.terminate()
