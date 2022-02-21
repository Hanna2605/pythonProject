import requests
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}
url = 'https://www.google.com/search?q=Eur+to+Usd&sxsrf=APq-WBs2fpCASujDdg9XtiyCxnT2uFiOLA%3A1645389997450&source=hp&ei=ragSYtCKGaWprgSUqZOYCQ&iflsig=AHkkrS4AAAAAYhK2vfB99qzbydyEId7_Wh-DmHQ6wIY7&ved=0ahUKEwiQlcCyk4_2AhWllIsKHZTUBJMQ4dUDCAc&uact=5&oq=Eur+to+Usd&gs_lcp=Cgdnd3Mtd2l6EAMyCQgAEEMQRhCCAjIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDoHCCMQ6gIQJzoECCMQJzoLCAAQgAQQsQMQgwE6CAgAEIAEELEDOhEILhCABBCxAxCDARDHARDRAzoECAAQQzoQCC4QsQMQgwEQxwEQ0QMQQzoKCAAQsQMQgwEQQzoECC4QQzoHCAAQgAQQCjoHCAAQsQMQQ1DiCFioJGCxKmgBcAB4AIAB2QGIAfYFkgEFOS4wLjGYAQCgAQGwAQo&sclient=gws-wiz'

r = requests.get(url, headers=headers)

pattern = re.compile(r'data-exchange-rate="[\d\.\d]+')
matches = pattern.finditer(r.text)
for match in matches:
    currency_data = match.group()
    break

pattern_currency = re.compile(r'\d\.\d+')
matches_currency = pattern_currency.finditer(currency_data)
for match in matches_currency:
    currency = match.group()
currency = float(currency)


def currency_convert_USD(currency, user_input):
    convert = user_input * currency
    return convert


def currency_convert_EUR(currency, user_input):
    convert = user_input / currency
    return convert


user_input = float(input('Please, enter your amount: '))
user_input_Currency = input('1. If EUR to USD, enter EUR\n'
                            '2. If USD to EUR, enter USD\n')
if user_input_Currency == '1':
    print(currency_convert_USD(currency, user_input))

elif user_input_Currency == '2':
    print(currency_convert_EUR(currency, user_input))
