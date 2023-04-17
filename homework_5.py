txt = 'Hello, world!'
assert txt[::-1] == '!dlrow ,olleH'
print('Reverse string: ', txt[::-1])

txt_length = len(txt)
assert len(txt) == 13

txt_list = list(txt)
assert txt_list == ['H', 'e', 'l', 'l', 'o', ',', ' ', 'w', 'o', 'r', 'l', 'd', '!']

txt_2 = f"{'|'.join((txt_list[::3]))}"
assert txt_2 == 'H|l| |r|!'


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


def count_symbols(string, k):
    count = 0
    for i in range(len(string)):
        if string[i] == k:
            count += 1
    return count


def str_to_dict_2(string):
    keys = list(string)
    values = list()
    for val in keys:
        amount = count_symbols(string, val)
        values.append(amount)
    res_dict = dict()
    for key in keys:
        for value in values:
            res_dict[key] = value
            values.remove(value)
            break
    return res_dict


assert str_to_dict_1(txt) == {'H': 1, 'e': 1, 'l': 3, 'o': 2, ',': 1,
                              ' ': 1, 'w': 1, 'r': 1, 'd': 1, '!': 1}
assert str_to_dict_2(txt) == {'H': 1, 'e': 1, 'l': 3, 'o': 2, ',': 1,
                              ' ': 1, 'w': 1, 'r': 1, 'd': 1, '!': 1}

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
    res_dict_sort = sorted(res_dict.items(), key=lambda k: k[1], reverse=False)
    return res_dict_sort[-1][0]


print(f"\nThe longest str in {str_list}: {search_longest_str(str_list)}.")

str_with_symbol = 'dfdf_asdea_asda_sdsd'


def divide_and_glue(string, symbol):
    list_string = string.split(symbol)
    list_string = sorted(list_string)
    new_string = symbol.join(list_string)
    return new_string


assert divide_and_glue(str_with_symbol, '_') == 'asda_asdea_dfdf_sdsd'

numbers = [119, 101, 108, 108, 32, 100, 111, 110, 101]


def ascii_codes(numbers):
    numbers_ascii = list()
    for num in numbers:
        num_ascii = str(num).encode(encoding='ascii')
        numbers_ascii.append(num_ascii)
    numbers_ascii = ', '.join(str(i) for i in numbers_ascii)
    print(f"\nString with ascii codes: \n{numbers_ascii}")
    assert type(numbers_ascii) == str


ascii_codes(numbers)
