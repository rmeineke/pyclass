'''
Defines Rupee class for Indian money.
'''
import currency_def

class Rupee(currency_def.Currency):
    exchange_rate = 67.14
    symbol = unichr(8377)
    tender = sorted([(value, 
                       currency_def.money_format.MoneyFormat(value).replace('$', symbol)
                       + " Bill")
                       for value in (5, 10, 20, 50, 100, 500, 1000)] 
                       + [(value, symbol + str(value) + " Coin")
                        for value in (1, 2, 5, 10)],
                        reverse=True)
'''
Rupee info via Wikipedia

Exchange rate per google ... 8/20/2016

    rupee = dollar.ExchangeFor(india_def.Rupee)


    print unicode(rupee), ":\n", unicode('\n'.join(rupee.MakeCurrency()))



A
import lab_08_Comprehensions.lab08_4 



'''
