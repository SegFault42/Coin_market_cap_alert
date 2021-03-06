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
twitter_account_sender = "" #without @
twitter_account_receiver = "" # without @

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def call_api():
    response = requests.get("https://api.coinmarketcap.com/v1/ticker/?convert=EUR&limit=10")
    if response.status_code != 200:
        print "API not respond"
        sys.exit(-1)
    return (response.json())

def store_data(devise, data):
    string = []
    money_name = data[devise]["name"]
    money_value_dollar = round(float(data[devise]["price_usd"]), 2)
    money_value_euro = round(float(data[devise]["price_eur"]), 2)
    percent_change_1h = data[devise]["percent_change_1h"]
    percent_change_24h = data[devise]["percent_change_24h"]

    string.append("#" + money_name + " = " + repr(money_value_dollar) + " $, " + repr(money_value_euro) + " E\n")
    string.append("last hour change : ")
    string.append(percent_change_1h + "%\n")
    string.append("last 24h change : ")
    string.append(percent_change_24h + "%\n")
    return (string)

def print_string(string):
    for index in range(len(string)):
        sys.stdout.write(string[index])
    sys.stdout.write("\n");

def tweet_alert(string, limit):
    split_string = string[0].split(" ")
    euro = split_string[2].split(".")
    tweet_current_value(''.join(string))
    if int(euro[0]) <= int(limit):
        tweet = "@" + twitter_account_receiver + "\n" + ''.join(string)
        try:
            api.update_status(status=tweet)
        except:
            pass

def tweet_current_value(tweet):
    try:
        api.update_status(status=tweet)
    except:
        pass

def usage():
    if len(sys.argv) != 3:
        print "Usage: python " + sys.argv[0] + " [limit bitcoin value] [limit ethereum value]"
        sys.exit(-1)

def main():
    usage()
    while True:
        data = call_api()

        string = store_data(bitcoin, data);
        print_string(string)
        tweet_alert(string, sys.argv[1])

        string = store_data(ethereum, data);
        print_string(string)
        tweet_alert(string, sys.argv[2])

        time.sleep(60 * 5) #Refresh every 5 minutes

if __name__ == '__main__':
    main()
