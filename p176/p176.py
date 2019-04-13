from time import time
from itertools import count

def n_split(n, depth=1, max_depth=1, previous_product=1, multiplicities=None):
    if depth == 1:
        n = 2*(n + 1) - 1
        multiplicities=[]
    for i in count(1):
        if depth == 1:
            product = 2*i - 1 # first prime - multiplicity is 2*n - 1
        else:
            product = previous_product*(2*i + 1) # subsequent primes - multiplicith is 2*n + 1
        if product > n: # break if number of splits is too high
            break
        if depth < max_depth:
            yield from n_split(n, depth=depth+1,
                                  max_depth=max_depth,
                                  previous_product=product,
                                  multiplicities=multiplicities+[i])
        else:
            if product == n:
                yield product, multiplicities+[i]

if __name__ == '__main__':
    PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    NSPLIT = 47547

    T0 = time()

    SOLUTION = -1
    for MAX_DEPTH in range(1, 11):
        for _, MULTI in n_split(NSPLIT, max_depth=MAX_DEPTH):
            PRODUCT = 1
            for P, M in zip(PRIMES, MULTI):
                PRODUCT *= pow(P, M)
            if SOLUTION == -1:
                SOLUTION = PRODUCT
            elif PRODUCT < SOLUTION:
                SOLUTION = PRODUCT

    print("Solution = {}".format(SOLUTION))
    print("Time elapsed = {:.2f}s".format(time()-T0))