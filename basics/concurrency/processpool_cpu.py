import math
from concurrent.futures import ProcessPoolExecutor

PRIMES = [
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419]


# use process for CPU intensive tasks
def is_prime(n):
    if n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        upper_bound = math.ceil(math.sqrt(n))
        for i in range(3, upper_bound, 2):
            if n % i == 0:
                return False
    return True


with ProcessPoolExecutor(3) as executor:
    # map blocks until the result is ready
    # this method chops the iterable data in a number of chunks that submits to the process pool as separate tasks.
    for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
        print('%d is prime: %s' % (number, prime))
