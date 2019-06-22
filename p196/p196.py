from time import time
from math import sqrt, ceil
from sympy import primerange, isprime

def time_elapsed(t):
    seconds = time() - t
    
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    
    return "{:.0f}h {:.0f}m {:f}s".format(hours, minutes, seconds)

def triangular(n):
    return n*(n+1)//2

def first(row):
    return triangular(row)+1

def last(row):
    return triangular(row+1)

def row_index(n):
    return ceil((sqrt(8*n + 1) - 1)/2)-1

def column_index(n, row=None):
    row = row_index(n) if row is None else row
    column = n - first(row)
    return column

def row_column_index(n):
    row = row_index(n)
    return (row, column_index(n, row))

def number(row, column):
    return first(row)+column

def neighbour_indices(row, column):
    if row == 0 and column == 0:
        return [(1, 0), (1, 1)]
    elif row == 1 and column == 0:
        return [(0, 0), (1, 1), (2, 0), (2, 1), (2, 2)]
    elif row == 1 and column == 1:
        return [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]
    else:
        if column == 0:
            return [(row-1, 0), (row-1, 1), (row, 1), (row+1, 0), (row+1, 1)]
        elif column == row-1:
            return [(row-1, column-1), (row-1, column), (row, column-1), (row, column+1), (row+1, column-1), (row+1, column), (row+1, column+1)]
        elif column == row:
            return [(row-1, column-1), (row, column-1), (row+1, column-1), (row+1, column), (row+1, column+1)]
        else:
            return [(row-1, column-1), (row-1, column), (row-1, column+1), (row, column-1), (row, column+1), (row+1, column-1), (row+1, column), (row+1, column+1)]

def neighbour_numbers(n):
    row, column = row_column_index(n)
    return [number(r, c) for r, c in neighbour_indices(row, column)]

def prime_neighbours(n):
    return [_n for _n in neighbour_numbers(n) if isprime(_n)]

def S(row_number):
    row_index = row_number - 1
    
    total = 0
    pl = list(primerange(first(row_index), last(row_index)+1))
    for i, prime in enumerate(pl):
        pn = prime_neighbours(prime)
        if len(pn) >= 2:
            total += prime
        elif len(pn) == 1:
            _pn = prime_neighbours(pn[0])
            if len(_pn) >= 2:
                total += prime
    return total


if __name__ == '__main__':
    print(S(10000))
    
    t0 = time()
    
    t1 = S(5678027)
    print(t1, time_elapsed(t0))
    t2 = S(7208785)
    print(t2, time_elapsed(t0))
    total = t1+t2

    print("Result: {}".format(total))
    print("Time elapsed: {}".format(time_elapsed(t0)))