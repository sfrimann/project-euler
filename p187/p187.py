import sympy
from time import time
from math import sqrt

if __name__ == '__main__':
    T0 = time()

    #LIMIT = 30
    LIMIT = 10**8

    PRIMES = list(sympy.sieve.primerange(1, LIMIT))

    TOTAL = 0
    while len(PRIMES) > 0:
        PRIME = PRIMES.pop(0)
        if PRIME > sqrt(LIMIT):
            break

        MAX_VAL = LIMIT // PRIME

        PRIMES = list(filter(lambda x: x <= MAX_VAL, PRIMES))

        TOTAL += len(PRIMES) + 1

    SECONDS = time() - T0

    MINUTES, SECONDS = divmod(SECONDS, 60)
    HOURS, MINUTES = divmod(MINUTES, 60)

    print("Result: {}".format(TOTAL))
    print("Time elapsed = {:.0f}h {:.0f}m {:f}s".format(HOURS, MINUTES, SECONDS))