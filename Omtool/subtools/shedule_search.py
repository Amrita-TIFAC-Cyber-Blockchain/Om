import os
import time
import sys
from colorama import Fore
import socket
import requests
import argparse
import utils.twitter_scraping
from utils import search_realname, search_username, ig_scrape, whois_lookup, webhook_spammer, ip_scanner, ip_lookup, \
    phonenumber_lookup, websearch, smsbomber, tokenlogger_generator, twitter_scraping
from subtools import omuser_search, omupi_search

import schedule
import time
def subschedule():
    print("its running...")
def omsheduler(search_query,time):
    schedule.every(int(time)).seconds.do(subschedule)

while True:
    schedule.run_pending()
    time.sleep(1)
