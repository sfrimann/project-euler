from time import time

def I(alpha, n, mod=10**9+7):
    alphaCn = alpha % mod # initialize to alpha choose 1
    n_incomplete = 0
    for i in range(1, alpha+1):
        if i == (alpha - 1):
            power_sum = (n + 1) % mod
        else:
            power_sum = ((1 - pow(alpha-i, n+1, mod)) * pow((1 - alpha + i), mod-2, mod)) % mod

        n_incomplete += (pow(-1, i+1, mod) * alphaCn * power_sum) % mod
        n_incomplete %= mod

        # update binomial coefficient recursively
        alphaCn *= (alpha - i) * pow(i+1, mod-2, mod)
        alphaCn %= mod

    return n_incomplete

if __name__ == '__main__':
    print("")
    print("Project Euler 657 solution")
    MOD = 10**9+7
    for ALPHA, N in zip([3, 3, 3, 10**7], [0, 2, 4, 10**12]):
        t0 = time()
        print("I({},{}) mod {} = {}, {:.2f}".format(ALPHA, N, MOD, I(ALPHA, N, mod=MOD), time()-t0))