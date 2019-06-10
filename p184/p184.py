from time import time

def time_elapsed(t):
    seconds = time() - t
    
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    
    return "{:.0f}h {:.0f}m {:f}s".format(hours, minutes, seconds)

if __name__ == '__main__':
    T0 = time()

    r_max = 105

    grid = []
    i0, i = 0, 0
    for y in range(-r_max, r_max+1):
        for x in range(-r_max, r_max+1):
            if x**2 + y**2 < r_max**2:
                if x == y == 0:
                    i0 = i
                grid.append((x, y))
                i += 1

    total = 0
    n = len(grid)
    for i in range(n):
        print(i, len(grid), time_elapsed(T0))
        a_1, a_2 = grid[i]
        if a_2 >= 0:
            break
        for j in range(i+1, n):
            b_1, b_2 = grid[j]
            x = a_1*b_2 - a_2*b_1
            if x == 0:
                continue
            x = x > 0
            for k in range(max(j+1, i0), n):
                c_1, c_2 = grid[k]
                y = b_1*c_2 - b_2*c_1
                if y == 0:
                    continue
                y = y > 0
                z = c_1*a_2 - c_2*a_1
                if z == 0:
                    continue
                z = z > 0
                if x == y and x == z:
                    total += 1

    print("Result: {}".format(total))
    print("Time elapsed = {}".format(time_elapsed(T0)))