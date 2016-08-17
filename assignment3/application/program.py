import sys
import os


#sys.path.insert(0, os.path.abspath('..'))
print()
print(sys.path)
print()
import application.driver.hw11_3


def main():
    application.driver.hw11_3.find_palindromes()
    
           
if __name__ == '__main__':
    main()

