from time import time
from itertools import product
from fractions import Fraction

if __name__ == '__main__':
    T0 = time()

    K = 35

    SOLUTIONS = []
    for BX, BY, BZ in product(range(2, K+1),repeat=3):
        for AX, AY, AZ in product(range(1, BX), range(1, BY), range(1, BZ)):
            if AX*BY*BZ + BX*AY*BZ == BX*BY*AZ:
                SOLUTION = True
            elif (AX*BY*BZ)**2 + (BX*AY*BZ)**2 == (BX*BY*AZ)**2:
                SOLUTION = True
            elif BX*AY*AZ + AX*BY*AZ == AX*AY*BZ:
                SOLUTION = True
            elif (BX*AY*AZ)**2 + (AX*BY*AZ)**2 == (AX*AY*BZ)**2:
                SOLUTION = True
            else:
                SOLUTION = False
            if SOLUTION:
                X, Y, Z = Fraction(AX, BX), Fraction(AY, BY), Fraction(AZ, BZ)
                S = X + Y + Z
                if S not in SOLUTIONS:
                    SOLUTIONS.append(S)

    T = sum(SOLUTIONS)
    U, V = T.numerator, T.denominator
    SECONDS = time() - T0

    MINUTES, SECONDS = divmod(SECONDS, 60)
    HOURS, MINUTES = divmod(MINUTES, 60)

    print("u + v = {}".format(U+V))
    print("Time elapsed = {:.0f}h {:.0f}m {:f}s".format(HOURS, MINUTES, SECONDS))