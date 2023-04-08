"""Module that provides doing homework_3"""


def main():
    """Homework"""
    def search_max(val_1, val_2):
        if val_1 > val_2:
            print('Max value: ', val_1)
            return val_1
        print('Max value: ', val_2)
        return val_2

    def search_min(val_1, val_2, val_3):
        if val_1 < val_2 and val_1 < val_3:
            print('Min value: ', val_1)
            return val_1
        if val_2 < val_1 and val_2 < val_3:
            print('Min value: ', val_2)
            return val_2
        print('Min value: ', val_3)
        return val_3

    def search_abs(val):
        if val >= 0:
            print('Absolute value: ', val)
            return val
        print('Absolute value: ', -val)
        return -val

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
    val_3 = int(input('Enter the third value (for min): '))
    search_max(val_1, val_2)
    search_min(val_1, val_2, val_3)

    val_4 = int(input('\nEnter the value to search for the abs: '))
    search_abs(val_4)

    print('\nEnter values to search sum.')
    val_5 = int(input('Enter the first value: '))
    val_6 = int(input('Enter the second value: '))
    print_sum(val_5, val_6)

    val_7 = int(input('\nEnter a value to determine its value: '))
    determ_pos_val(val_7)


if __name__ == '__main__':
    main()
