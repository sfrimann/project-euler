from time import time
from sympy.ntheory import primerange

def p659(kmax):
    t0 = time()

    primes = list(primerange(1, 2*kmax))
    primes = [prime for prime in primes if (prime - 1) % 4 == 0 ]

    total = 0
    for k in range(1, kmax+1):
        rem = 4*k*k + 1
        biggest_prime_divisor = 1

        for prime in primes:
            while prime*prime <= rem and rem % prime == 0:
                rem //= prime
                biggest_prime_divisor = prime
            if prime*prime > rem:
                break
        total += biggest_prime_divisor if rem == 1 else rem
    return total, time()-t0

if __name__ == '__main__':
    for KMAX in [10**3, 10**4, 10**5, 10**6, 10**7]:
        TOTAL, SECONDS = p659(KMAX)
        MINUTES, SECONDS = divmod(SECONDS, 60)
        HOURS, MINUTES = divmod(MINUTES, 60)

        print("")
        print("kmax = {}".format(KMAX))
        print("total = {}".format(TOTAL))
        print("Time elapsed = {:.0f}h {:.0f}m {:f}s".format(HOURS, MINUTES, SECONDS))