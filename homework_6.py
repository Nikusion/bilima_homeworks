"""Module that provides doing homework 4"""
import random
import string
import time


def sum_of_list_items(arr):
    """A recursive function that returns the sum of values
    in a list (elements can be of integer type or list)"""
    if len(arr) == 1:
        return arr[0]
    new_arr = []
    for item in arr:
        if isinstance(item, list):
            for items in item:
                new_arr.append(items)
        else:
            new_arr.append(item)
    return new_arr[0] + sum_of_list_items(new_arr[1:])


def cycle_words(values, size):
    """A function that returns a list of existing
    elements repeated a given number of times."""
    arr = []
    while len(arr) < size:
        for value in values:
            arr.append(value)
            if len(arr) >= size:
                break
    return arr


def password_checker(password):
    """A function that checks passwords element by element."""
    for real_pass_char, passed_pass_char in zip(PASSWORD, password):
        if real_pass_char != passed_pass_char:
            return
        time.sleep(0.1)


def password_cracker():
    """A function that selects a password.
    Selects based on the function password_checker()."""
    symbols = string.ascii_letters
    cracked_password = []
    for k in range(4):
        for letter in symbols:
            start = time.time()
            cracked_password.append(letter)
            password_checker(cracked_password)
            end = time.time()
            if end - start > len(cracked_password) * 0.1:
                break
            cracked_password.pop()
    return ''.join(str(k) for k in cracked_password)


if __name__ == '__main__':
    list_items = [1, 2, [3, [4, 5, [6, 7]], 8]]
    print(sum_of_list_items(list_items))

    arr_string = ['a', 'b', 'c']

    print(cycle_words(arr_string, 5))

    PASSWORD = ''.join(random.choices(string.ascii_letters, k=4))

    print(PASSWORD)

    print(password_cracker())
