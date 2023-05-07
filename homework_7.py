"""Module that provides doing homework 7"""

import random


def retry(attempts=5, desired_value=None):
    """This function repeats the specified code a
    specified number of times and checks the return value."""

    def decorate(func):
        def wrapper(*args, **kwargs):
            for i in range(attempts):
                result = func(*args, **kwargs)
                if result == desired_value:
                    print('The desired result was obtained: ', result,
                          'on attempt:', i)
                    break
            if result != desired_value:
                print('The desired result could not be achieved!')

        return wrapper

    return decorate


@retry(desired_value=3)
def get_random_value_with_default_attempts():
    """This function returns a random value between 1 and 5."""
    return random.choice((1, 2, 3, 4, 5))


@retry(desired_value=[1, 2])
def get_random_values_with_default_attempts(choices, size=2):
    """This function returns a random list value of
    two values taken from another list."""
    return random.choices(choices, k=size)


@retry(attempts=7, desired_value=3)
def get_random_value():
    """This function is equivalent
    get_random_value_with_default_attempts()."""
    return random.choice((1, 2, 3, 4, 5))


@retry(attempts=2, desired_value=[1, 2, 3])
def get_random_values(choices, size=2):
    """This function is equivalent
    get_random_values_with_default_attempts()."""
    return random.choices(choices, k=size)


def write_to_file(path):
    file = open(path, 'w')  # w = write, r = read
    file.write('skhfbsdhfb\n')
    file.flush()
    file.write('s;jdsfnkdfjv\n')
    file.flush()
    file.write('kjfbksdhbvsdkj\n')
    file.flush()
    file.close()

def copy_contents(path_1, path_2):
    with open(path_1, 'r') as file_1, open(path_2, 'w') as file_2:
        for line in file_1:
            file_2.write(line)


if __name__ == '__main__':
    get_random_value()
    get_random_value_with_default_attempts()
    get_random_values_with_default_attempts([1, 2, 3, 4])
    get_random_values_with_default_attempts([1, 2, 3, 4], 2)
    get_random_values_with_default_attempts([1, 2, 3, 4], size=2)
    get_random_values_with_default_attempts(choices=[1, 2, 3, 4], size=2)
    get_random_values([1, 2, 3, 4])
    get_random_values([1, 2, 3, 4], 3)
    get_random_values([1, 2, 3, 4], size=1)

    write_to_file('file.txt')
    copy_contents('file.txt', 'file_copy.txt')


