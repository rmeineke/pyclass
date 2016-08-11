# hw07_1.py
"""Check to see if a string identifier meets proper Python strictures.
"""

import keyword


def IsValidIdentifier(s):
    """Check validity of python identifier.
    
    Args:
        param1 (str): The string to check for validity.
    
    Returns:
        tuple: Returns True for success, False for failure and 
        includes an explanatory string.
        (True, "Valid!") for example."""

    # look for illegal characters
    for char in s:
        if char != '_' and not char.isalnum():
            return False, "{:>20} -> Invalid: '{}' is not allowed.".format(s, char)

    # check for keywords
    if keyword.iskeyword(s):
        return False, '{:>20} -> Invalid: this is a keyword!'.format(s)

    # if the first character is a number return false
    if s[0].isdigit():
        return False, '{:>20} -> Invalid: first symbol must be alphabetic or underscore'.format(s)

    return True, '{:>20} -> Valid!'.format(s)
