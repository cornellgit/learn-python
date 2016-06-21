def fib(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return n


def fib_seq(n):
    seq = []
    a, b = 0, 1
    while b < n:
        seq.append(b)
        a, b = b, a + b
    return seq
