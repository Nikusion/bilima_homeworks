a_int = 3
b_int = 4

c_union = a_int==b_int
print(c_union)

CONST = 'hello'
print(CONST + ' ' + str(a_int-b_int))

d_list = [a_int, b_int, c_union, CONST]
print(set(d_list))

e_tuple1 = (1, 2, 2.5, 'Nika', False)
e_tuple2 = (2, 5, True, 'B')

f_union = e_tuple1 + e_tuple2

print(list(f_union))

g_dict = {
    'age' : 1,
    'name' : 'Nika',
    3 : 'qwerty',
    True : None,
    False : [1, 2, 3, 'pool'],
    17.1 : {
        'surname' : 'Bilima',
        1 : 5
    },
    (1, 2, 3, 6, 'Jessie', None) : (2, 6, True)
}
print(g_dict)