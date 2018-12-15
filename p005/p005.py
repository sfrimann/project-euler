from sympy import primerange
from math import log

def p005(k):
    n = 1
    for prime in list(primerange(1, k+1)):
        exponent = int(log(k, 10)/log(prime, 10))
        n *= prime**exponent
    return n

if __name__ == '__main__':

    for LIMIT in [10, 20]:
        print("")
        print("limit = {}".format(LIMIT))
        print("Result for ndigit = 2: {}".format(p005(LIMIT)))
