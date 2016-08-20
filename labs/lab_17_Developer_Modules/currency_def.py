#!/usr/bin/env python
# coding: utf-8   # necessary for python not to complain
                  # about "¥" in the strings
"""A base class, Currency, for inheriting into any country's
currency class.
"""
import sys
import os
if __name__ == '__main__': 
    sys.path.insert(0, "..") 
else:                        
    sys.path.insert(0, os.path.join(os.path.split(__file__)[0], '..'))

import lab_08_Comprehensions.lab08_4 as money_format

class Currency(float):
    """Base class for all currencies.

    To add a currency, subclass and provide three attributes:
    symbol, exchange_rate (amount per dollar), and a sequence of
    tender [(amount, name), (amount, name) ...] sorted so that
    the largest amount is first.
    """
    def __add__(self, other):
        """Exchanges the right-hand operand to the currency type
        of the left-hand operand and and adds them, returning
        the type of the left-hand operand.
        """
        
        if type(self) == type(other):
            return self.__class__(float(self) + float(other))
        return self.__class__(float(self) 
                              + float(other.ExchangeFor(self.__class__)))
            
    def __eq__(self, other):
        if abs(self - other.ExchangeFor(self.__class__)) <= .0001:
            return True
        return False

    def ExchangeFor(self, what):
        """Exchanges the self for the equivalent value in
        "what", where "what" is a currency class.
        """
        dollars = self/self.exchange_rate
        other =  getattr(what, "exchange_rate") * dollars
        return what(other)

    def MakeCurrency(self):
        """Returns a list of the bills and coins needed to make the amount."""
        if self < 0:
            return []
        return_parts = []
        amount = self
        for value, name in self.tender:
            how_many, amount = divmod(amount, value)
            if how_many:
                if how_many > 1:
                    if name.endswith('y'):
                        name = name[:-1] + 'ies'
                    else:
                        name = name + 's'
                return_parts += ["%5d %s" % (how_many, name)]
        return return_parts

    def __repr__(self):
        return """%s('%f')""" % (self.__name__, self)
    
    def __str__(self):
        return money_format.MoneyFormat(self).replace('$', self.symbol)

