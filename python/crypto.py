import requests
import json


def getprice(currency_money, currrency_crypto):
    response = requests.get(
        f"https://api.coingecko.com/api/v3/simple/price?ids={currency_crypto}&vs_currencies={currency_money}")
    if response.status_code == 404:
        return 404
    json = response.json()
    return json[currency_crypto][currency_money]


# def jprint(obj):
# created formattedstring of the of the Python JSON string
# text = json.dumps(obj, sort_keys=True, indent=4)
# print(text)
currency_money = input("What currency do you want? (usd or aud): ")
currency_crypto = input("What crypto do you wish to acess? (bitcoin,ethereum or dogecoin): ")



print("$"+ str(getprice(currency_money, currency_crypto)))


