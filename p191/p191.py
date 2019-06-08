from time import time
from functools import lru_cache

@lru_cache(maxsize=2**20)
def count_prize_days(ndays, late_once=False, absent2=False, absent1=False):
    if ndays == 0:
        return 1
    
    total = 0
    for status in ['O', 'A', 'L']:
        if status == 'L' and late_once: # already late once
            pass
        elif (absent2 is True) and (absent1 is True) and (status == 'A'): #absent for three consecutive days
            pass
        else:
            _late_once = True if status == 'L' else late_once
            _absent2 = absent1
            _absent1 = True if status == 'A' else False
            total += count_prize_days(ndays-1, late_once=_late_once, absent2=_absent2, absent1=_absent1)
    return total

if __name__ == '__main__':
    T0 = time()
    
    LIMIT = 30
    
    TOTAL = count_prize_days(LIMIT)

    SECONDS = time() - T0

    MINUTES, SECONDS = divmod(SECONDS, 60)
    HOURS, MINUTES = divmod(MINUTES, 60)

    print("Result: {}".format(TOTAL))
    print("Time elapsed = {:.0f}h {:.0f}m {:f}s".format(HOURS, MINUTES, SECONDS))