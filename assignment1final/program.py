import hw07_1


def main():
    print()
    print('Test supplied data first:')
    print('===================================================')
    print()
    strings = ('x', '_x', '2x', 'x,y ', 'yield', 'is_this_good')

    # run the program against the test data provided in the
    # assignment
    for input_str in strings:
        (return_value, return_string) = hw07_1.IsValidIdentifier(input_str)
        print(return_string)

    # now test it interactively
    print()
    print()
    print('Test interactively:')
    print('===================================================')
    print()

    input_str = None
    while True:
        input_str = input('Please enter a string ([Enter] to quit): ')
        if input_str == '':
            break
        (return_value, return_string) = hw07_1.IsValidIdentifier(input_str)
        print(return_string)
        print()


if __name__ == '__main__':
    main()
