from time import time
from math import sqrt
from itertools import cycle

def continued_fraction_periodic(d):

    sd = sqrt(d)
    p, q = 0, 1

    terms = []
    pq = {}

    while (p, q) not in pq:
        pq[(p, q)] = len(terms)
        terms.append(int((p + sd)/q))
        # black magic to determine period
        p = terms[-1]*q - p
        q = (d - p**2)//q
        yield terms[-1]

    i = pq[(p, q)]
    
    for term in cycle(terms[i:]):
        yield term

def best_approximation_convergents(n, bound):
    cf_iter = continued_fraction_periodic(n) # continued fraction iterator
    
    s0 = next(cf_iter)
    s1 = next(cf_iter)
    
    # initialize rational approximations
    p = [None, s0, s0*s1 + 1] # numerator
    q = [None,  1, s1] # denominator
    
    for a in cf_iter:
        p[0], q[0] = p[1], q[1]
        p[1], q[1] = p[2], q[2]
        p[2], q[2] = p[0] + a*p[1], q[0] + a*q[1]

        if q[2] > bound:
            break
    return p[:2], q[:2], a

def best_approximation_semiconvergents(n, bound):
    
    p, q, a = best_approximation_convergents(n, bound)
    
    p_best, q_best = p[1], q[1] # current estimate of best approximation
    
    if a == 1: # no semi convergents. Convergent is best approximation
        return p_best, q_best

    if a % 2 == 0: # if a is even we have to check if first semi convergent better approximation
        p_sc, q_sc = p[0] + a*p[1]//2, q[0] + a*q[1]//2
        
        if q_sc > bound: # if semi convergent exceeds bound return best convergent approximation
            return p_best, q_best

        if q_best**2*abs(p_sc**2 - q_sc**2*n) < q_sc**2*abs(p_best**2 - q_best**2*n):
            p_best, q_best = p_sc, q_sc
    
    alim = a//2 + 1
    
    for _a in range(a//2+1, a):
        p_sc, q_sc = p[0] + _a*p[1], q[0] + _a*q[1]
        
        if q_sc > bound:
            break
        
        p_best, q_best = p_sc, q_sc
    
    return p_best, q_best



if __name__ == '__main__':
    T0 = time()

    LIMIT = 10**5
    BOUND = 10**12

    SQUARES = [i**2 for i in range(2, int(sqrt(LIMIT))+1)]

    TOTAL = 0
    for N in range(2, LIMIT+1):
        if N in SQUARES:
            continue

        P, Q = best_approximation_semiconvergents(N, BOUND)
        TOTAL += Q

    SECONDS = time() - T0

    MINUTES, SECONDS = divmod(SECONDS, 60)
    HOURS, MINUTES = divmod(MINUTES, 60)

    print("Result: {}".format(TOTAL))
    print("Time elapsed = {:.0f}h {:.0f}m {:f}s".format(HOURS, MINUTES, SECONDS))