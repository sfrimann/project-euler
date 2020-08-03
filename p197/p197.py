from time import time

def time_elapsed(t):
    seconds = time() - t
    
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    
    return "{:.0f}h {:.0f}m {:f}s".format(hours, minutes, seconds)

def f(x):
    return int(2**(30.403243784-x**2))*10**(-9)

if __name__ == '__main__':
    print(f(-1))
    print(f(f(-1)))
    
    t0 = time()
    
    un = -1
    for n in range(1, 10**3+1):
        if n % 10**9 == 0:
            print(n//10**9, un, un*10**9*2, time_elapsed(t0))
        un = f(un)

    unp1 = f(un)

    total = un + unp1
    print("Result: {}".format(total))
    print("Time elapsed: {}".format(time_elapsed(t0)))