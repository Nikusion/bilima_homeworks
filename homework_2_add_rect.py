def search_point_rect(vert_1, vert_3, point):
    if(vert_1[0] <= point[0] <= vert_3[0] and
            vert_1[1] <= point[1] <= vert_3[1]):
        return True
    return False

print('\tPlease, when you enter point coordinates, separate them with a space.')
vertice_1_input = input('Enter the coordinates of the first vertice of the rectangle: ')
vertice_1 = tuple(int(n) for n in vertice_1_input.split())

vertice_3_input = input('Enter the coordinates of the second vertice of the rectangle: ')
vertice_3 = tuple(int(n) for n in vertice_3_input.split())

point_input = input('Enter the coordinates of the point: ')
point = tuple(int(n) for n in point_input.split())

if search_point_rect(vertice_1, vertice_3, point):
    print('Point enters the rectangle.')
else:
    print('Point is outside the rectangle')
