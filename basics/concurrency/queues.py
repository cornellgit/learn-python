import multiprocessing as mp
import time
from os import getpid as pid


# A queue returns a process shared queue, is thread and process safe
class Producer(mp.Process):
    def __init__(self, q):
        mp.Process.__init__(self)
        self.q = q

    def run(self):
        for i in range(5):
            self.q.put(i)
            print("p-%s:%s" % (pid(), i))
            time.sleep(1)
        print('exit p-%s' % (pid(),))


class Consumer(mp.Process):
    def __init__(self, q):
        mp.Process.__init__(self)
        self.q = q

    def run(self):
        while not self.q.empty():
            print("c-%s:%s" % (pid(), self.q.get()))
            time.sleep(2)
        print('exit c-%s' % (pid(),))


queue = mp.Queue()
p_list = [Producer(queue), Producer(queue), Consumer(queue), Consumer(queue)]

for proc in p_list:
    proc.start()

for proc in p_list:
    proc.join()
