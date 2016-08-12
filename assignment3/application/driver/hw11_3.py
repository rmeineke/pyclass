import os
import sys

sys.path.insert(0, os.path.abspath('../utils'))

import hw11_2

def check_directory_for_palindromes(directory):
    print('Entering check_directory_for_palindromes')
    print(directory)
    
    #os.path.walk ... deprecated to os.walk in python3
    os.walk(directory, hw11_2.Palindromize, 'Checking: ')
    
    
def main():
    check_this_directory = '../../application'
    for directory, subdir_list, file_list in os.walk(check_this_directory, topdown=True):
        print('Checking directory: {}'.format(directory))
        for filename in file_list:
            print('\t{}'.format(filename))
            print('\t\topen file')
            print('\t\tgrab words from file')
            print(hw11_2.Palindromize('ahhhhha'))

    os.walk(directory, hw11_2.Palindromize2, 'Checking: ')


if __name__ == '__main__':
    main()
