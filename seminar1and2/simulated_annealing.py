import sys, random, math

def algorithm(x_points, y_points, z_points):
    T = len(x_points)*len(y_points)
    x_index,y_index = 0,0
    z = sys.maxsize
    z_test = 0
    finished = False
    alfa = 0.9
    while y_index < len(z_points) and not finished:
        x_index = 0
        while x_index < len(z_points[y_index]):
            z_test = z_points[y_index][x_index]
            diff =  (z - z_test)        
            if diff < 0:
                r = random.uniform(0,1)
                exponential = diff/T
                try:
                    boltzman = math.exp(exponential)
                    if r < boltzman:
                        z = z_test # move to a worse solution, hopefully temporary
                    else:
                        finished = True
                        break
                except OverflowError:
                    z = z_test
            else:
                z = z_test
            x_index += 1
            T *= alfa
        y_index += 1

    x = x_points[x_index - 1]
    y = y_points[y_index - 1]
    return (x,y,z)