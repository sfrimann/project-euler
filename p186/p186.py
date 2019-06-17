from time import time
from functools import lru_cache
from itertools import count

def time_elapsed(t):
    seconds = time() - t
    
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    
    return "{:.0f}h {:.0f}m {:f}s".format(hours, minutes, seconds)

@lru_cache(maxsize=2**8)
def S(k, mod=10**6):
    if k >= 56:
        return (S(k-24) + S(k-55)) % mod
    else:
        return (100003 - 200003*k + 300007*k**3) % mod

def call_generator(mod=10**6):
    for n in count(1):
        caller = S(2*n-1, mod=mod)
        called = S(2*n, mod=mod)
        if caller != called:
            yield caller, called

class Node:
    """Node in disjoint set data structure"""

    def __init__(self, id):

        self.id = id
        self.parent = self
        self.rank = 0
        self.size = 1

    def find(self):
        """find by path halving"""
        x = self
        while x.parent != x:
            x.parent = x.parent.parent
            x = x.parent
        return x

def union(x, y):
    x_root = x.find()
    y_root = y.find()

    # x and y are already in the same set
    if x_root == y_root:
        return

    # x and y are not in same set, so we merge them
    if x_root.size < y_root.size:
        x_root, y_root = y_root, x_root # swap xRoot and yRoot

    # merge yRoot into xRoot
    y_root.parent = x_root
    x_root.size = x_root.size + y_root.size

if __name__ == '__main__':
    T0 = time()
    
    LIMIT = 10**6
    PM_ID = 524287

    GOAL = LIMIT - LIMIT//100

    CALLERS = [Node(i) for i in range(LIMIT)]

    CG = call_generator()

    NCALLS = 0
    PM_SIZE = 1
    while PM_SIZE < GOAL:
        CALLER_ID, CALLED_ID = next(CG)
        NCALLS += 1

        union(CALLERS[CALLER_ID], CALLERS[CALLED_ID])

        PM_SIZE = CALLERS[PM_ID].find().size

    print("Result: {}".format(NCALLS))
    print("Time elapsed = {}".format(time_elapsed(T0)))