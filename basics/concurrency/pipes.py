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


def transform(func, conn):
    """receive input from pipe, transform it"""
    try:
        while True:
            # Blocks until there its something to receive.
            # Raises EOFError if there is nothing left to receive and the other end was closed.
            i = conn.recv()
            print('transform:', func(i))
    except EOFError:
        conn.close()


c_1, c_2 = mp.Pipe()
p1 = mp.Process(target=send, args=(c_1,))
p2 = mp.Process(target=transform, args=(lambda x: x ** 2, c_2,))

p1.start()
p2.start()
p1.join()
p2.join()


#
#
# def f(conn):
#     conn.send([42, None, 'hello'])
#     conn.close()
#
# if __name__ == '__main__':
#     c1, c2 = mp.Pipe()
#     p = mp.Process(target=f, args=(c1,))
#     p.start()
#     print (c2.recv())   # prints "[42, None, 'hello']"
#     p.join()
