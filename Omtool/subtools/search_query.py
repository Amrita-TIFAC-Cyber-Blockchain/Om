import os
import time
import sys
from colorama import Fore
import socket
import requests
import argparse
import schedule
import time
import logging
import utils.twitter_scraping
from utils import search_realname, search_username, ig_scrape, whois_lookup, webhook_spammer, ip_scanner, ip_lookup, \
    phonenumber_lookup, websearch, smsbomber, tokenlogger_generator, twitter_scraping
from subtools import omuser_search, omupi_search, omphone_search

"""
this function is used perform a search for a given query

Args:
    search_type : Type of the query 
    query : The search query

Raises:
    Invalid option when search_type is out of the boundry
"""
def searchquery(search_type,query):
    if search_type=="a":
        omuser_search.omuser_search(query)
        omupi_search.omupi_search(query)
    elif search_type=="b":
        omphone_search.omphone("+91"+query)
        omupi_search.omupi_search(query)
    elif search_type=="c":
        print("\n")
        split_query = query.split("@")
        # websearch.Search(split_query[0])
        omupi_search.omupi_search(split_query[0])
    elif search_type=="d":
        omupi_search.omupi_search(query)
    elif search_type=="e":
        utils.twitter_scraping.scraping_options()

"""
this function is used perform a search for a given query

Args:
    query_type : Type of the Search
    search_type : Type of the query 
    query : The search query
    timer : Time to search in scheduled search

Raises:
    Invalid option when search_type is out of the boundry
"""

def omsearcher(query_type,search_type,query,timer):
    if query_type=="3" or query_type=="4":
        searchquery(search_type,query)
        logging.info("Performing Live search")
    elif query_type=="2" or query_type=="1":
        schedule.every(timer).minutes.do(searchquery)
        logging.info("Performing Periodical search")
    # elif query_type=="1":
    else:
        print(Fore.RED + "Invalid option!")
        time.sleep(1)
        logging.info("Invalid search")
    

        



