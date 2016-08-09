import hw07_1


def main():
    print()
    print('Test supplied data first:')
    print('===================================================')
    print()
    strings = ('x', '_x', '2x', 'x,y ', 'yield', 'is_this_good')

    # run the program against the test data provided in the
    # assignment
    for str in strings:
        (return_value, return_string) = hw07_1.IsValidIdentifier(str)
        print(return_string)

    # now test it interactively
    print()
    print()
    print('Test interactively:')
    print('===================================================')
    print()

    str = None
    while True:
        str = input('Please enter a string ([Enter] to quit): ')
        if str == '':
            break
        (return_value, return_string) = hw07_1.IsValidIdentifier(str)
        print(return_string)
        print()


if __name__ == '__main__':
    main()
