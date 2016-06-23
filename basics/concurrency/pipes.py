# 1. Returns a pair of connection objects connected by a pipe
# 2. every object has send/receive methods
# data in a pipe may become corrupted if two processes (or threads) try to read from or write
# to the same end of the pipe at the same times

# this code doesn't terminate strange

import multiprocessing as mp


def send(conn):
    """send obj to pipe"""
    for i in range(10):
        conn.send(i)
        print("send:", i)
    conn.close()


def transform(func, pipe):
    """receive input from pipe, transform it"""
    conn = pipe[1]
    pipe[0].close()
    try:
        while True:
            # Blocks until there its something to receive.
            # Raises EOFError if there is nothing left to receive and the other end was closed.
            i = conn.recv()
            print('transform:', func(i))
    except EOFError:
        conn.close()
        # to get EOF I need to make sure c_1 is closed in all processes including main


pipe = (c_1, c_2) = mp.Pipe()

p_list = [mp.Process(target=send, args=(c_1,)),
          mp.Process(target=transform, args=(lambda x: x ** 2, pipe))]

for proc in p_list:
    proc.start()

c_1.close()
for proc in p_list:
    proc.join()
