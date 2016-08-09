# hw07_1.py
"""Check to see if a string meets
proper Python strictures. Returns
a tuple value (True or False, return_str).

(True, "Valid!") for example
"""
    

def IsValidIdentifier(s):
"""Check validity of python identifier.

Args:
    param1 (str): The first parameter.

Returns:
    tuple: The return value. True for success, False otherwise.
    Return also includes explanatory string.
    (True, "Valid!") for example"""
    
    return_str = ''
    
    # test for keywords
    if keyword:
        return_str = 'Invalid: this is a keyword!'
        pass
        
    # test for question marks
    elif str[0] not '_' or srt[0]:
        return_str = 'Invalid: first symbol must be alphabetic or underscore.'

    elif has bad char:
        return_str = 'Invalid: ’?’ is not allowed.'
        
    else:
        return (True, 'Valid!')
        
