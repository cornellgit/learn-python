# semaphore is constituted of an internal variable that identifies the number of concurrent access to a resource
# 1. acquire() decreases the variable, release() increment
# 2. it allows access  this variable>0
# semaphore event purpose is to synchronize the computation of two or more threads
# TODO in which patterns are Semaphore useful?
# A particular use of semaphores is the mutex.
# A mutex is nothing but a semaphore with an internal variable initialized to the value 1

import random
import threading

from os import getpid as pid


def producer():
    global num
    num = random.randint(0, 100)
    print('p-%s: %s' % (pid(), num))
    sem.release()
    # this wakes up the waiting consumer thread


def consumer():
    print("consumer is waiting.")
    sem.acquire()
    print('c-%s: %s' % (pid(), num))


num = 0
sem = threading.Semaphore(0)

for i in range(5):
    threads = [threading.Thread(target=producer),
               threading.Thread(target=consumer)]
    for t in threads:
        t.start()

    for t in threads:
        t.join()
