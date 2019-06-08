from time import time

def hyperexp(a, k, mod=None):
    if k == 1:
        return a
    else:
        if mod is None:
            return pow(a, hyperexp(a, k-1))
        else:
            return pow(a, hyperexp(a, k-1, mod), mod)

if __name__ == '__main__':
    T0 = time()

    MOD = 10**8

    RESULT = hyperexp(1777, 1855, MOD)

    SECONDS = time() - T0

    MINUTES, SECONDS = divmod(SECONDS, 60)
    HOURS, MINUTES = divmod(MINUTES, 60)

    print("Result: {}".format(RESULT))
    print("Time elapsed = {:.0f}h {:.0f}m {:f}s".format(HOURS, MINUTES, SECONDS))