from time import time
from math import sqrt

def kmax(n):
    return int((sqrt(8*n + 1) - 1)/2)

def nmin(k):
    return k*(k+1)//2

def m(nmax, k):
    _nmin = nmin(k)
    if _nmin >= nmax:
        return 0
    
    ndiff, rem = divmod(nmax - _nmin + 1, k)
    
    return k*nmin(ndiff) + (ndiff+1)*rem

def M(n, mod=10**9+7):
    total = 0
    for k in range(1, kmax(n)+1):
        total += m(n, k) % mod
    return total % mod

if __name__ == '__main__':
    SECONDS = time()

    N = 10**16
    result = M(N)
    
    SECONDS = time() - SECONDS

    MINUTES, SECONDS = divmod(SECONDS, 60)
    HOURS, MINUTES = divmod(MINUTES, 60)

    print("M(10**6) % 1000000007 = {}".format(result))
    print("Time elapsed = {:.0f}h {:.0f}m {:f}s".format(HOURS, MINUTES, SECONDS))