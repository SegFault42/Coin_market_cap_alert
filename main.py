# -*- coding: utf-8 -*-
import requests
import json
import sys
import tweepy
import time

bitcoin = 0
ethereum = 1

consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""
twitter_account = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def call_api():
    response = requests.get("https://api.coinmarketcap.com/v1/ticker/?convert=EUR&limit=10")
    if response.status_code != 200:
        print "API not respond"
        sys.exit(-1)
    data = response.json()
    return (data)

def store_data(devise, data):
    string = []
    money_name = data[devise]["name"]
    money_value_dollar = data[devise]["price_usd"]
    money_value_euro = data[devise]["price_eur"]
    percent_change_1h = data[devise]["percent_change_1h"]
    percent_change_24h = data[devise]["percent_change_24h"]

    string.append(money_name + " = " + money_value_dollar + "$, " + money_value_euro + u"\u20AC\n")
    string.append("last hour change : ")
    if (percent_change_1h[0] != '-'):
        string.append("+" + percent_change_1h + "%\n")
    else:
        string.append(percent_change_1h + "%\n")
    string.append("last 24h change : ")
    if (percent_change_1h[0] != '-'):
        string.append("+" + percent_change_24h + "%\n")
    else:
        string.append(percent_change_24h + "%\n")
    return string

def print_string(string):
    for index in range(len(string)):
        sys.stdout.write(string[index])
    sys.stdout.write("\n");

def tweet_string(string):
    tweet = twitter_account + "\n" + ''.join(string)
    api.update_status(status=tweet)

def main():
    while True:
        data = call_api()

        string = store_data(bitcoin, data);
        print_string(string)
        tweet_string(string)

        string = store_data(ethereum, data);
        print_string(string)
        tweet_string(string)

        #time.sleep(60 * 30) #sleep 30 minutes

if __name__ == '__main__':
    main()
