"""Helper functions involving prime numbers"""

from collections import defaultdict

def trial_division(n):
    """Find prime factors of n with trial division"""
    factors = defaultdict(int)

    factor = 2
    while n % factor == 0:
        factors[factor] += 1
        n //= factor

    factor = 3
    while factor*factor <= n:
        if n % factor == 0:
            factors[factor] += 1
            n //= factor
        else:
            factor += 2

    factors[n] += 1

    return factors
