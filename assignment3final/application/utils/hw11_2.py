def Palindromize(phrase):
    
    # make sure everything passed in is seen as a string object
    # the numbers (12321, etc.) caused a crash without this
    phrase = str(phrase)
    
    #too short
    if len(phrase) < 4:
        return None
    
    #lowercase, strip spaces/punctuation, and reverse it
    string = phrase.lower()
    string = ''.join(ch for ch in string if ch.isalnum())
    reversed_string = string[::-1]
    if string != reversed_string:
        return None
    return reversed_string

         
if __name__ == '__main__':
    main()

