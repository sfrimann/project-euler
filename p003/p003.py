
LIMIT = 600851475143

def p003(n):
    """Find largest prime factor of n by trial division"""
    factor = 2
    while n % factor == 0:
        n //= factor

    factor = 3
    while factor*factor <= n:
        if n % factor == 0:
            n //= factor
        else:
            factor += 2

    return n

if __name__ == '__main__':

    for limit in [13195, 600851475143]:
        print("Result for n == {}: {}".format(limit, p003(limit)))
