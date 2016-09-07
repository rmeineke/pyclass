'''
Defines Dollar class for USA money.
'''

import currency_def

class Dollar(currency_def.Currency):
    exchange_rate = 1.0
    symbol = '$'
    tender = sorted([(value, currency_def.money_format.MoneyFormat(value)
                      + " Bill")
                     for value in (1, 5, 10, 20, 50, 100, 1000)]
                    + [(.50, 'Half Dollar'), (.25, 'Quarter'),
                       (.10, 'Dime'), (.05, 'Nickel'), (.01, 'Penny')],
                    reverse=True)

    
