import hw07_1


def main():
    DATA = ('x', '_x', '2x', 'x,y ', 'yield', 'is_this_good')
    for str in DATA:
        hw07_1.IsValidIdentifier(str)
   

    
if __name__ == '__main__':
    main()
