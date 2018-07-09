
LIMIT = 4*10**6

def p002_brute_force():
    """Brute-force solution"""
    f_nm2, f_nm1 = 1, 1

    total = 0
    while f_nm1 < LIMIT:
        if f_nm1 % 2 == 0:
            total += f_nm1

        f_nm2, f_nm1 = f_nm1, f_nm2+f_nm1

    return total

def p002_even_recurrence():
    """Even recurrence solution"""
    e_nm2, e_nm1 = 2, 8

    total = 2
    while e_nm1 < LIMIT:
        total += e_nm1

        e_nm2, e_nm1 = e_nm1, 4*e_nm1 + e_nm2

    return total


if __name__ == '__main__':

    print("Brute force solution.   : {}".format(p002_brute_force()))
    print("Even recurrence solution: {}".format(p002_even_recurrence()))

fn = fn-2 + fn-1
   = fn-4 + fn-3 + fn-3 + fn-2
   = fn-4 + fn-3 + fn-3 + fn-4 + fn-3
   = 3*fn-3 + 2*fn-4
   = 3*fn-3 + fn-4 + fn-6 + fn-5
   = 4*fn-4 + fn-6