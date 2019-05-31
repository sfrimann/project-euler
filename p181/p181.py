from functools import lru_cache
from time import time

def calculate_order(nb, nw):
    return nb*(N_WHITE+1) + nw

@lru_cache(maxsize=2**20)
def n_double_partition(n_black, n_white, porder=None):
    if n_black == 0 and n_white == 0:
        return 1

    porder = calculate_order(n_black, n_white) if porder is None else porder
    
    total = 0
    for black in range(n_black, -1, -1):
        for white in range(n_white, -1, -1):
            if black == 0 and white == 0:
                continue
            order = calculate_order(black, white)
            if order > porder:
                continue
            tup = (black, white)
            total += n_double_partition(n_black-black, n_white-white, porder=order)
    
    return total

if __name__ == '__main__':
    T0 = time()

    N_BLACK, N_WHITE = 60, 40

    RESULT = n_double_partition(N_BLACK, N_WHITE)
    SECONDS = time() - T0

    MINUTES, SECONDS = divmod(SECONDS, 60)
    HOURS, MINUTES = divmod(MINUTES, 60)

    print(f"result = {RESULT}")
    print("Time elapsed = {:.0f}h {:.0f}m {:f}s".format(HOURS, MINUTES, SECONDS))