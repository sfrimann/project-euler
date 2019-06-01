from time import time

def Pm(m):
    l = 2/(m+1)
    prod = 1
    for i in range(1, m+1):
        prod *= (i*l)**i
    return int(prod)

if __name__ == '__main__':
    T0 = time()

    TOTAL = 0
    for M in range(2, 16):
        TOTAL += Pm(M)

    SECONDS = time() - T0

    MINUTES, SECONDS = divmod(SECONDS, 60)
    HOURS, MINUTES = divmod(MINUTES, 60)

    print("Result: {}".format(TOTAL))
    print("Time elapsed = {:.0f}h {:.0f}m {:f}s".format(HOURS, MINUTES, SECONDS))