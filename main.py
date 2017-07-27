# -*- coding: utf-8 -*-
import requests
import json
import sys

bitcoin = 0
ethereum = 1

def call_api():
    response = requests.get("https://api.coinmarketcap.com/v1/ticker/?convert=EUR&limit=10")
    if response.status_code != 200:
        print "API not respond"
        sys.exit(-1)
    data = response.json()
    return (data)

def print_money(devise, data):
    money_name = data[devise]["name"]
    money_value_dollar = data[devise]["price_usd"]
    money_value_euro = data[devise]["price_eur"]
    percent_change_1h = data[devise]["percent_change_1h"]
    percent_change_24h = data[devise]["percent_change_24h"]

    print money_name + " = " + money_value_dollar + "$, " + money_value_euro + u"\u20AC"

    sys.stdout.write("last hour change : ")
    if (percent_change_1h[0] != '-'):
        print "+" + percent_change_1h + "%"
    else:
        print percent_change_1h + "%"
    sys.stdout.write("last 24h change : ")
    if (percent_change_1h[0] != '-'):
        print "+" + percent_change_24h + "%"
    else:
        print percent_change_24h + "%"

data = call_api()
print_money(bitcoin, data);
print ""
print_money(ethereum, data);
