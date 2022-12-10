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

def omuser_search(query):
    print("\n")
    print("*********************************************************************************************************\n")
    print("***********************************  UserName(Powered by H4x-tool)  *************************************\n")
    print("*********************************************************************************************************\n")
    websearch.Search(query)
    username = query.replace(" ", "_")
    print("\n")
    search_realname.facebook(username)
    search_realname.linkedin(username)
    search_realname.whitepages(username)
    search_realname.peoplefinders(username)
    print("\n")
    search_username.instagram(username)
    search_username.pinterest(username)
    search_username.twitter(username)
    search_username.youtube(username)
    search_username.github(username)
    search_username.stackoverflow(username)
    search_username.steam(username)
    search_username.reddit(username)
    # search_username.tiktok(username)
    # search_username.twitch(username)
