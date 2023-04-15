def unique_val(*numbers):
    return list(set(numbers))


print('\tResult of task 1: ')
print(unique_val(1, 2, 3, 4, 3, 5, 'qw', 'qw', 2))

task_2_args = {'a': 4, 'b': 8}
task_2_args_2 = {'a': 4, 'b': 8, 'user_type': 'Worker'}


def task_2(**kwargs):
    kwargs.setdefault('user_type', 'Student')
    print('Number of arguments passed: ', len(kwargs))
    print('User_type: ', kwargs['user_type'])


print('\n\tResult of task 2 without return: ')
task_2(**task_2_args)
task_2(**task_2_args_2)


def task_2_2(**kwargs):
    kwargs.setdefault('user_type', 'Student')
    return len(kwargs), kwargs['user_type']


res_1 = task_2_2(**task_2_args)
res_2 = task_2_2(**task_2_args_2)
print('\n\tResult of task 2 with return: ')
print(f"Number of arguments passed: {res_1[0]}. \nUser_type: {res_1[1]}.")
print(f"Number of arguments passed: {res_2[0]}. \nUser_type: {res_2[1]}.")


def func_f(val_1):
    def func_g(val_2):
        return val_1 * val_2

    return func_g


print('\n\tResult of task 4 (args = 6,3): ')
print(func_f(6)(3))

print('\n\tResult of task 5 (size 5): ')
def print_square(size, count):
    if size < 1 or count == 0:
        return
    print('*' * size)
    print_square(size, count-1)

print_square(5, 5)
