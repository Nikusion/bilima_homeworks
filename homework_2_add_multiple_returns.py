def sum_and_diff(val_1, val_2):
    sum = val_1 + val_2
    difference = val_1 - val_2
    return sum, difference

val_1 = int(input('Value 1: '))
val_2 = int(input('Value 2: '))

sum, diff = sum_and_diff(val_1, val_2)
print('Sum of values: {}. \nDifference of values: {}.'.format(sum, diff))