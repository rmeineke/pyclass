def Palindromize(phrase):
    if len(phrase) < 4:
        return 'Too short: {}'.format(phrase)
    
    string = phrase.lower()
    string = ''.join(ch for ch in string if ch.isalnum())
    
    return string
    
def main():
    
    test_strings = ('Murder for a jar of red rum', 12321, 'nope', 'abcbA', 3443, 'what', 'Never odd or even', 'Rats live on no evil star')
    
    for string in test_strings:
        print(string)
        #print(Palindromize(string))
    

if __name__ == "__main__":
    main()
