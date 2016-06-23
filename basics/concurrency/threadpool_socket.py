from concurrent.futures import ThreadPoolExecutor
from socket import socket


# an echo server
def echo(sock):
    msg = sock.recv(65536)
    sock.sendall(msg)
    sock.close()


def server(addr):
    pool = ThreadPoolExecutor(2)
    sock = socket()
    sock.bind(addr)
    sock.listen(5)
    while True:
        client_sock, client_addr = sock.accept()
        pool.submit(echo, client_sock, client_addr)


server(('', 15000))
