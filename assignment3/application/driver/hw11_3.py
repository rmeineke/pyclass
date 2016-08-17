import os
import sys

# add the application directory to the path
sys.path.insert(0, '..')

# and import the palindrome module
import utils.hw11_2


def ask_user_for_directory():
    while True:
        resp = input('Which directory do you wish to search? ')
        if os.path.isdir(resp):
            return resp
        else:
            print("Oops, that doesn't seem to be a directory.\n")
    
    
def find_palindromes():
    
    check_this_directory = ask_user_for_directory()
       
    #walk the chosen directory
    for directory, subdir_list, file_list in os.walk(check_this_directory, topdown=True):
        print('\nChecking directory: {}'.format(directory))
        
        for filename in file_list:
            filename = os.path.join(directory, filename)
            print('\t{}'.format(filename))
            with open(filename, 'r') as input_file:
                try:
                    for line in input_file:
                        ret_string = utils.hw11_2.Palindromize(line)
                        if ret_string:
                            print('\t\tPALINDROME FOUND: {}'.format(ret_string))
                except UnicodeDecodeError:
                    print('\t[decode error: {}]'.format(filename))
                except:
                    print('\t[error reading from: {}]'.format(filename))

           
if __name__ == '__main__':
    find_palindromes()
