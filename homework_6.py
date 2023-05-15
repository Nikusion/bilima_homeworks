"""Module that provides doing homework 4"""
import random
import string
import time


def sum_of_list_items(arr):
    """A recursive function that returns the sum of values
    in a list (elements can be of integer type or list)"""
    total = 0
    for item in arr:
        if isinstance(item, int):
            total += item
        elif isinstance(item, list):
            total += sum_of_list_items(item)

    return total


def cycle_words(values, size):
    """A function that returns a list of existing
    elements repeated a given number of times."""
    return [values[i % len(values)] for i in range(size)]


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
    cracked_password = ''
    for k in range(4):
        for letter in symbols:
            start = time.time()
            password_checker(cracked_password + letter)
            end = time.time()
            if end - start > (len(cracked_password) + 1) * 0.1:
                cracked_password += letter
                break
    return cracked_password


if __name__ == '__main__':
    assert sum_of_list_items([]) == 0
    assert sum_of_list_items([1, 2]) == 3
    assert sum_of_list_items([1, [2, 3, [4], [5, 6, [7]]]]) == 28

    assert cycle_words(['a', 'b', 'c'], 7) == ['a', 'b', 'c', 'a', 'b', 'c', 'a']
    assert cycle_words(['a', 'b', 'c'], 1) == ['a']
    assert cycle_words(['a', 'b', 'c'], 0) == []

    PASSWORD = ''.join(random.choices(string.ascii_letters, k=4))
    assert password_cracker() == PASSWORD
