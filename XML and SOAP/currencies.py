import osa
import math


def get_travel_cost(file):
    client = osa.Client("http://fx.currencysystem.com/webservices/CurrencyServer4.asmx?WSDL")
    res = 0
    with open(file, 'r') as f:
        for line in f:
            cur_from = line.split()[2]
            amount = int(line.split()[1])
            res += math.ceil(client.service.ConvertToNum(None, cur_from, 'RUB', amount, True, None, None, None))
            # print(line,math.ceil(client.service.ConvertToNum(None, cur_from, 'RUB', amount, True, None, None, None)))

    return res


print('Стоимость путешествия в рублях:{}'.format(get_travel_cost('currencies.txt')))
