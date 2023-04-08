"""Module that provides doing homework_3"""


def main():
    """Homework"""
    def search_max(val_1, val_2):
        if val_1 > val_2:
            print('Max value: ', val_1)
            return val_1
        if val_1 < val_2:
            print('Max value: ', val_2)
            return val_2
        if val_1 == val_2:
            print('The numbers are equal to each other.\nMax value: ', val_1)
            return val_1
        return 0

    def search_min(val_1, val_2):
        if val_1 > val_2:
            print('Min value: ', val_2)
            return val_2
        if val_1 < val_2:
            print('Min value: ', val_1)
            return val_1
        if val_1 == val_2:
            print('The numbers are equal to each other.\nMin value: ', val_1)
            return val_1
        return 0

    def search_abs(val):
        if val >= 0:
            print('Absolute value: ', val)
            return val
        if val < 0:
            print('Absolute value: ', -val)
            return -val
        return 0

    def print_sum(val_1, val_2):
        print(val_1 + val_2)

    def determ_pos_val(val):
        if val > 0:
            print('Value ', val, ' is positive.')
        elif val < 0:
            print('Value ', val, ' is negative.')
        else:
            print('Value ', val, ' is equal to 0.')

    print('Enter values to compare.')
    val_1 = int(input('Enter the first value: '))
    val_2 = int(input('Enter the second value: '))
    search_max(val_1, val_2)
    search_min(val_1, val_2)

    val_3 = int(input('\nEnter the value to search for the abs: '))
    search_abs(val_3)

    print('\nEnter values to search sum.')
    val_4 = int(input('Enter the first value: '))
    val_5 = int(input('Enter the second value: '))
    print_sum(val_4, val_5)

    val_6 = int(input('\nEnter a value to determine its value: '))
    determ_pos_val(val_6)


if __name__ == '__main__':
    main()
