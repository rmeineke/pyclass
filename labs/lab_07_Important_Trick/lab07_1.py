#!/usr/bin/env python
"""lab07_1.py Provides a TranslateToKeypad function that,
when passed a string of alphanumeric characters, returns a
string of digits.  
"""
def TranslateToKeypad(word):
    """Returns the word, translated to the telephone keypad equivalent:
    abc -> 2  ghi -> 4   mno -> 6   tuv -> 8
    def -> 3  jkl -> 5  pqrs -> 7  wxyz -> 9
    Other characters get passed on.
    """
    KEY_MAP = ('abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz')

    translated_word = ''
    for ch in word.lower():
        hit = 2
        for key_letters in KEY_MAP:
            if ch in key_letters:
                translated_word += str(hit)
                break
            hit += 1
        else:
            translated_word += ch
    return translated_word

def main():
    """Tests the TranslateToKeypad function."""
    
    DATA = "peanut", "salt", "lemonade", "good time", ":10", "Zilch"
    for word in DATA:
        print "%10s -> %s" % (word, TranslateToKeypad(word))

if __name__ == "__main__":
    main()
"""
$ lab07_1.py
    peanut -> 732688
      salt -> 7258
  lemonade -> 53666233
 good time -> 4663 8463
       :10 -> :10
     zilch -> 94524
$"""
