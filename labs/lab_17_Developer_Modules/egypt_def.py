'''
Defines EgyptionPound class for Egyptian money.
'''

import currency_def

class Pound(currency_def.Currency):
    exchange_rate = 5.96810   # 5/27/11   www.oanda.com
    symbol = unichr(163)
    tender = [(200, symbol + '200 Bill'),
              (100, symbol + '100 Bill'),
              (50, symbol + '50 Bill'),
              (20, symbol + '20 Bill'),
              (10, symbol + '10 Bill'),
              (5, symbol + '5 Bill'),
              (1, symbol + '1 Bill'),
              (1, '1 Pound Coin'),
              (0.5, '50 Piastres Coin'),
              (0.5, '50 Piastres Bill'),
              (0.25, '25 Piastres Coin'),
              (0.25, '25 Piastres Bill'),
              (0.10, '10 Piastres Coin'),
              (0.05, '5 Piastres Coin')]
