'''
Defines Yen class for Japanese money.
'''
import currency_def

class Yen(currency_def.Currency):
    exchange_rate = 81.1076  # 5/27/11 www.x-rates.com
    symbol = unichr(165)
    tender = sorted([(value, 
                      currency_def.money_format.MoneyFormat(value).replace('$', symbol)
                      + " Bill")
                     for value in (1000, 2000, 5000, 10000)] 
                    + [(value, symbol + str(value) + " Coin")
                       for value in (1, 5, 10, 50, 100, 500)],
                    reverse=True)

