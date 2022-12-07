import os
import time
import sys
from colorama import Fore
import socket
import requests
import argparse
import schedule
import time
import utils.twitter_scraping
from utils import search_realname, search_username, ig_scrape, whois_lookup, webhook_spammer, ip_scanner, ip_lookup, \
    phonenumber_lookup, websearch, smsbomber, tokenlogger_generator, twitter_scraping
from subtools import omuser_search

def omupi_search(target):
    target
    main_url = 'https://upibankvalidator.com/api/upiValidation?upi='
    upi_ids = ['apl','oksbi','okhdfcbank','sbi','okicici','axisbank','ikwik','pnb','hdfc','idfcbank','okaxis','abfspay','ybl','barodampay','upi','paytm','yapl','dbs','yesbankltd','utbi','united','ubi','rajgovhdfcbank','pockets','payzapp'
    ,'mahb','kaypay','imobile','idbibank','hdfcbank','ezeepay','eazypay','cnrb','centralbank','cboi','cbin','boi','yesbank','wasbi','waicici','wahdfcbank','waaxis','unionbankofindia','unionbank','uco','ubio','timecosmos','tapicici','sib'
    ,'rbl','pingpay','kotak','kmbl','kbl','jupiteraxis','indus','indianbank','idbi','icici','ibl','hsbc','freecharge','federal','fbl','dlb','citigold','citi','bandhan','axl','axisb','aubank','allbank']

    if len(target) > 2:
        if target.find('@')!=-1:
            response = requests.post(main_url+target).json()
            if response['isUpiRegistered']:
                print(f"{Fore.BLUE}✅ UPI Holder Name: {response['name']}",f"| UPI platform: {target.partition('@')[2]}")
            else:
                print(f"{Fore.WHITE}❌ Invalid UPI Not found in",i)
        else:
            for i in upi_ids:
                response = requests.post(main_url+target+'@'+i).json()
                if response['isUpiRegistered']:
                            # print('found')
                    print(f"{Fore.GREEN}✅ UPI Holder Name: {Fore.RED}{response['name']}",f"| UPI platform: {i}")
                else:
                                        # print(Fore.RED)
                                        # print('Invalid UPI Not found in',i)  
                    print(f"{Fore.WHITE}❌ Invalid UPI Not found in",i)