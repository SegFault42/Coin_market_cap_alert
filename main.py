# -*- coding: utf-8 -*-

import requests
import json
import sys

response = requests.get("https://api.coinmarketcap.com/v1/ticker/?convert=EUR&limit=10")
data = response.json()

money_name = data[0]["name"]
money_value_dollar = data[0]["price_usd"]
money_value_euro = data[0]["price_eur"]
percent_change_1h = data[0]["percent_change_1h"]
percent_change_24h = data[0]["percent_change_24h"]

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






