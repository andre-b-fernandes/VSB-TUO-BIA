import sys

def algorithm(x_points, y_points, z_points):
    x_index,y_index = 0,0
    z = sys.maxsize
    z_test = 0
    while y_index < len(z_points) and z_test < z:
        x_index = 0
        while x_index < len(z_points[y_index]):
            z_test = z_points[y_index][x_index]
            if z_test > z:
                break
            z = z_test
            x_index += 1
        y_index +=1
        
    x = x_points[x_index - 1]
    y = y_points[y_index - 1]
    return (x,y,z)