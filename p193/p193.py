from time import time
from functools import reduce
from sympy import primerange
from itertools import combinations

import operator

def time_elapsed(t):
    seconds = time() - t
    
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    
    return "{:.0f}h {:.0f}m {:f}s".format(hours, minutes, seconds)

def prod(iterable):
    return reduce(operator.mul, iterable, 1)

if __name__ == '__main__':
    t0 = time()
    
    exponent = 50

    limit = 2**exponent
    sqrt_limit = 2**(exponent//2)

    sq_primes = [p**2 for p in primerange(1, sqrt_limit+1)]

    previous_products = [(1, 0)]
    next_products = []

    total = 0
    for n_comb in range(1, len(sq_primes)+1):
        if prod(sq_primes[:n_comb]) >= limit:
            break
        print(n_comb, len(previous_products), time_elapsed(t0))
        for j, (prev_prod, ibeg) in enumerate(previous_products):
            for i, sq_prime in enumerate(sq_primes[ibeg:]):
                product = prev_prod*sq_prime
                if product >= limit:
                    break
                if i+ibeg+1 < len(sq_primes):
                    if product*sq_primes[i+ibeg+1] < limit:
                        next_products.append((product, i+ibeg+1))
                total += (-1)**(n_comb+1) * ((limit-1)//product)
        previous_products = next_products
        next_products = []

    print("Result: {}".format(limit-total-1))
    print("Time elapsed: {}".format(time_elapsed(t0)))