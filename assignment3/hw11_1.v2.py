def main():
    print(GiveAsciiChart())
    
    
def GiveAsciiChart():
    # here is the one-liner!   
    #
    # and they say that PERL is hard to read!
    # this works ... up to and including the formatting
    return str(''.join(' ' * (3 - len(str(num + 32))) + str(num + 32) + ':  ' + ch + '\t\t' + "\n" * (num % 4 == 3) for num, ch in enumerate([chr(x) for x in range(32, 127)])))
    
    
    # broken down to be a bit more readable
    # return str(''.join(' ' * (3 - len(str(num + 32))) +     \
                # str(num + 32) + ':  ' + ch + '\t\t' +       \
                # "\n" * (num % 4 == 3)                       \
                # for num, ch in enumerate(                   \
                # [chr(x) for x in range(32, 127)]            \
            # )))
    
    
    # and here is a commented version
    # return str(''.join(                                     \
    
                ## formatting:
                ## print "spaces" times (3 - length_of_the_ascii_value)
                # ' ' * (3 - len(str(num + 32))) +            \
                
                ## ascii value, colon, character, and a couple of tabs
                # str(num + 32) + ':  ' + ch + '\t\t' +       \
                
                ## formatting:
                ## print "newlines" only when the expression evaluates to one
                # "\n" * (num % 4 == 3)                       \
                
                ## grab the item number (num) and character (ch) from
                ## the enumeration
                # for num, ch in enumerate(                   \
                
                ## translate to the character representation for
                ## each 'x' in the specified range
                # [chr(x) for x in range(32, 127)]            \
            # )))


if __name__ == "__main__":
    main()
