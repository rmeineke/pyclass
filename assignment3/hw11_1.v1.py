def main():
    print(GiveAsciiChart())
    
    
def GiveAsciiChart():
    ret_string = ''
    for x in range(32,127):
        ret_string += '{:>3}: {:>3}\t'.format(x, chr(x))
        if (x % 4) == 3:
            ret_string += '\n'
    return ret_string
    

if __name__ == "__main__":
    main()
