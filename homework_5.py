txt = 'Hello, world!'
print(txt[::-1])

txt_length = len(txt)
print(txt_length)

txt_list = list(txt)
print(txt_list)
print(txt_list.count('l'))

txt_2 = f"str {'|'.join((txt_list[::3]))}"
print(txt_2)


def str_to_dict_1(string):
    keys = list(string)
    values = list()
    for val in keys:
        amount = keys.count(val)
        values.append(amount)
    res_dict = dict()
    for key in keys:
        for value in values:
            res_dict[key] = value
            values.remove(value)
            break
    return res_dict

def count_str(str, k):
    count = 0
    for i in range(len(str)):
        if(str[i] == k):
            count += 1
    return count
def str_to_dict_2(string):
    keys = list(string)
    values = list()
    for val in keys:
        amount = count_str(string, val)
        values.append(amount)
    res_dict = dict()
    for key in keys:
        for value in values:
            res_dict[key] = value
            values.remove(value)
            break
    return res_dict

print(str_to_dict_1(txt))
print(str_to_dict_2(txt))

str_list = ['a', 'avcfdfdfdfd', 'sedefds']

def search_longest_str(list_string):
    lengths = list()
    for string in list_string:
        length = len(string)
        lengths.append(length)
    res_dict = dict()
    for string in list_string:
        for len_s in lengths:
            res_dict[string] = len_s
            lengths.remove(len_s)
            break
    print(res_dict)
    res_dict_sort = sorted(res_dict.items(), key = lambda x: x[1], reverse = False)
    return res_dict_sort[-1]


search_longest_str(str_list)
print(search_longest_str(str_list)[0])
