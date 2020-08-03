from time import time
from math import pi

def p_old(a, total=0, rem=pi**2/6, depth=0, max_depth=10):
    proba = 1./2**depth
    if total > a:
        return proba
    if (total+rem) <= a:
        return 0
    if depth >= max_depth:
        return proba/2
    delta = 1./(depth+1)**2
    return p_old(a, total=total+delta, rem=rem-delta, depth=depth+1, max_depth=max_depth) + \
           p_old(a, total=total, rem=rem-delta, depth=depth+1, max_depth=max_depth)

def p(a, total=0, rem=None, depth=0, max_depth=10):
    if rem is None:
        rem = sum([1./i**2 for i in range(1, max_depth+1)])
    proba = 1./2**depth
    if total > a:
        return proba
    if (total+rem) <= a:
        return 1./2**(max_depth+1)
    delta = 1./(depth+1)**2
    return p(a, total=total+delta, rem=rem-delta, depth=depth+1, max_depth=max_depth) + \
           p(a, total=total, rem=rem-delta, depth=depth+1, max_depth=max_depth)

if __name__ == '__main__':
    SECONDS = time()

    A, MAX_DEPTH = 0.5, 38
    
    result = p(A, max_depth=MAX_DEPTH)
    #r0 = p_old(A, max_depth=MAX_DEPTH)
    
    SECONDS = time() - SECONDS

    MINUTES, SECONDS = divmod(SECONDS, 60)
    HOURS, MINUTES = divmod(MINUTES, 60)

    print(result)
    print("p(a) = {:.9f}".format(result))
    print("Time elapsed = {:.0f}h {:.0f}m {:f}s".format(HOURS, MINUTES, SECONDS))