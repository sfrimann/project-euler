from math import gcd, e
from time import time

if __name__ == '__main__':
    T0 = time()

    LIMIT = 10**4

    RESULT = 0
    for N in range(5, LIMIT+1):
        #f(k) = (n/k)**k has maximum at k = n/e
        K = round(N/e)

        DENOM = K // gcd(N, K)

        # terminating decimals only have prime factors 2 and 5
        # do trial division
        while DENOM % 2 == 0: DENOM //= 2
        while DENOM % 5 == 0: DENOM //= 5

        RESULT += -N if DENOM == 1 else N

    MINUTES, SECONDS = divmod(SECONDS, 60)
    HOURS, MINUTES = divmod(MINUTES, 60)

    print(f"result = {RESULT}")
    print("Time elapsed = {:.0f}h {:.0f}m {:f}s".format(HOURS, MINUTES, SECONDS))