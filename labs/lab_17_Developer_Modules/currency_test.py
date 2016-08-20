#!/usr/bin/env python
# coding: utf-8   # necessary for python not to complain
                  # about "¥" in the strings
"""
Test for currency classes.
"""
import currency_def
import egypt_def
import japan_def
import usa_def

def TestValue(value):
    print 'value', value, ':'
    egyptian_pound = egypt_def.Pound(value)
    dollar = egyptian_pound.ExchangeFor(usa_def.Dollar)
    yen = dollar.ExchangeFor(japan_def.Yen)
    print unicode(egyptian_pound), \
          ":\n", unicode('\n'.join(egyptian_pound.MakeCurrency()))
    print dollar, ':\n', '\n'.join(dollar.MakeCurrency())
    print unicode(yen), ":\n", unicode('\n'.join(yen.MakeCurrency()))
    another_pound = yen.ExchangeFor(egypt_def.Pound)
    try:
        assert another_pound == egyptian_pound
    except:
        print "broke:", unicode(another_pound), unicode(egyptian_pound)
        print float(another_pound), float(egyptian_pound)
        raise

    thrice = egyptian_pound + dollar + yen
    assert thrice ==  egyptian_pound + egyptian_pound + egyptian_pound

def RandomTest(tries=2):
    import random
    for test in range(tries):
        value = random.random() * (10 **random.randrange(7))
        TestValue(value)

def main():
    for value in (1000, 100.01, 32.232):
        TestValue(value)
    RandomTest(2)
    
if __name__ == '__main__':
    main()
"""
$ currency_test.py
value 1000 :
£1,000.00 :
    5 £200 Bills
$167.56 :
    1 $100.00 Bill
    1 $50.00 Bill
    1 $10.00 Bill
    1 $5.00 Bill
    2 $1.00 Bills
    1 Half Dollar
    1 Nickel
¥13,590.19 :
    1 ¥10,000.00 Bill
    1 ¥2,000.00 Bill
    1 ¥1,000.00 Bill
    1 ¥500 Coin
    1 ¥50 Coin
    4 ¥10 Coins
value 100.01 :
£100.01 :
    1 £100 Bill
$16.76 :
    1 $10.00 Bill
    1 $5.00 Bill
    1 $1.00 Bill
    1 Half Dollar
    1 Quarter
¥1,359.15 :
    1 ¥1,000.00 Bill
    3 ¥100 Coins
    1 ¥50 Coin
    1 ¥5 Coin
    4 ¥1 Coins
value 32.232 :
£32.23 :
    1 £20 Bill
    1 £10 Bill
    2 £1 Bills
    2 10 Piastres Coins
$5.40 :
    1 $5.00 Bill
    1 Quarter
    1 Dime
    1 Nickel
¥438.04 :
    4 ¥100 Coins
    3 ¥10 Coins
    1 ¥5 Coin
    3 ¥1 Coins
value 90.7788796644 :
£90.78 :
    1 £50 Bill
    2 £20 Bills
    1 50 Piastres Coin
    1 25 Piastres Coin
$15.21 :
    1 $10.00 Bill
    1 $5.00 Bill
    2 Dimes
    1 Penny
¥1,233.70 :
    1 ¥1,000.00 Bill
    2 ¥100 Coins
    3 ¥10 Coins
    3 ¥1 Coins
value 145.882439366 :
£145.88 :
    1 £100 Bill
    2 £20 Bills
    1 £5 Bill
    1 50 Piastres Coin
    1 25 Piastres Coin
    1 10 Piastres Coin
$24.44 :
    1 $20.00 Bill
    4 $1.00 Bills
    1 Quarter
    1 Dime
    1 Nickel
    4 Pennies
¥1,982.57 :
    1 ¥1,000.00 Bill
    1 ¥500 Coin
    4 ¥100 Coins
    1 ¥50 Coin
    3 ¥10 Coins
    2 ¥1 Coins
"""
