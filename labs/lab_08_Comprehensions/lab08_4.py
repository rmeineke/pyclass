#!/usr/bin/env python
"""lab08_4.py
MoneyFormat(amount) returns a money representation of the amount
"""

def MoneyFormat(amount):
    """MoneyFormat(amount) returns a money representation of the amount."""
    neg = False
    if amount < 0:
        amount *= -1
        neg = True
    money = "%.2f" % amount
    chars = list(money)
    chars.reverse()
    parts = chars[:3]
    for i, ch in enumerate(chars[3:]):
        if i > 0 and i % 3 == 0:
            parts += ','
        parts += ch
    parts.reverse()
    if neg:
        parts.insert(0, '-$')
    else:
        parts.insert(0, '$')
    return ''.join(parts)

def main():
    print MoneyFormat(-123.21)
    print MoneyFormat(3)
    print MoneyFormat(14.3123)
    print MoneyFormat(1234567.89)
    print MoneyFormat(-88.88)

if __name__ == '__main__':
    main()
"""
$ lab08_4.py
-$123.21
$3.00
$14.31
$1,234,567.89
-$88.88
$
"""
