from time import time
from math import sqrt, pi

def time_elapsed(t):
    seconds = time() - t
    
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    
    return "{:.0f}h {:.0f}m {:f}s".format(hours, minutes, seconds)

def fourth_curvature(k1, k2, k3):
    k4p = k1 + k2 + k3 + 2*sqrt(k1*k2 + k2*k3 + k3*k1)
    k4m = k1 + k2 + k3 - 2*sqrt(k1*k2 + k2*k3 + k3*k1)
    return k4p, k4m

def update_area(circles):
    a = 0
    for curvature, kisses in circles:
        a += pi*(1/curvature)**2
    return a

if __name__ == '__main__':
    
    t0 = time()
    
    area = 0 # area covered by inscriped circles

    ## zeroth iteration
    k0 = -1 # surrounding circle curvature
    k1 = 2.1547005383792524 # curvature of circles in zeroth iteration
    circles = [(k1, (k0, k1, k1)), (k1, (k1, k0, k1)), (k1, (k1, k1, k0))] # zeroth iteration circles
    area += update_area(circles) # areas of circles in first iteration
    print(0, area, round(1-area/pi, 8), time_elapsed(t0))

    ## first iteration
    k2 = max(fourth_curvature(k0, k1, k1)) # curvature edge circles
    k3 = max(fourth_curvature(k1, k1, k1)) # curvature center circle
    circles = [(k2, (k0, k1, k1)), (k2, (k1, k0, k1)), (k2, (k1, k1, k0)), (k3, (k1, k1, k1))]
    area += update_area(circles)
    print(1, area, round(1-area/pi, 8), time_elapsed(t0))

    ## subsequent iterations
    new_circles = []
    for i in range(2, 11):
        new_circles = []
        for k0, (k1, k2, k3) in circles:
            k4 = max(fourth_curvature(k0, k1, k2))
            new_circles.append((k4, (k0, k1, k2)))

            k4 = max(fourth_curvature(k0, k2, k3))
            new_circles.append((k4, (k0, k2, k3)))

            k4 = max(fourth_curvature(k0, k3, k1))
            new_circles.append((k4, (k0, k3, k1)))
        circles = new_circles[:]
        area += update_area(circles)
        print(i, area, round(1-area/pi, 8), time_elapsed(t0))

    print("Result: {}".format(round(1-area/pi, 8)))
    print("Time elapsed: {}".format(time_elapsed(t0)))