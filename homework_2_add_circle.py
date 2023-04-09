import math

def search_point_circle(center, radius, point):
    segment = math.sqrt((center[0]-point[0])**2+(center[1]-point[1])**2)
    if radius - segment > 0:
        print('Point enters the circle.')
    elif radius - segment == 0:
        print('Point is on the circle.')
    else:
        print('Point is outside the circle.')

print('\tPlease, when you enter point coordinates, separate them with a space.')
center_input = input('Enter the coordinates of the center of the circle: ')
center = tuple(int(n) for n in center_input.split())

radius = float(input('Enter the length of the radius: '))

point_input = input('Enter the coordinates of the point: ')
point = tuple(int(n) for n in point_input.split())

search_point_circle(center, radius, point)