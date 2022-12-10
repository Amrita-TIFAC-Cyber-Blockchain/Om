# -*- coding: utf-8 -*-

'''
Om - OSINT me 

To perform individual search using unique identifiers like Phone Number, Usernames, Email IDs and 
UPI address.

This is specifically customized for TN Police Hackathon 2022.

Tool Developed by Team ModSouls, TIFAC-CORE in Cyber Security, Amrita Vishwa Vidyapeetham, Coimbatore.

'''
import datetime
import os
import time
import sys
from colorama import Fore
import socket
import requests
import argparse
import logging
import utils.twitter_scraping
from utils import search_realname, search_username, ig_scrape, whois_lookup, webhook_spammer, ip_scanner, ip_lookup, \
    phonenumber_lookup, websearch, smsbomber, tokenlogger_generator, twitter_scraping
from subtools import search_query


if os.name == "nt":
    os.system("cls")
    os.system("title Om Tool")
if os.name == "posix":
    os.system("clear")


def install(package):
    os.system(f"{sys.executable} -m pip install {package}")


def internet_check():
    try:
        socket.create_connection(("www.google.com", 80))
        print(Fore.GREEN + "\n[!] Internet Connection is Available!")
        return None
    except OSError:
        print(Fore.RED + "\n[=!] Warning! Internet Connection is Unavailable!")
        return None


def main():
    print(Fore.CYAN + """
[+]    
|
|   ██████╗  ███╗   ███╗      ███╗   ███╗  ██████╗   ██████╗   ███████╗   ██████╗   ██╗   ██╗  ██╗       ███████╗ 
|  ██╔═══██╗ ████╗ ████║      ████╗ ████║ ██╔═══██╗  ██╔══██╗  ██╔════╝  ██╔═══██╗  ██║   ██║  ██║       ██╔════╝
|  ██║   ██║ ██╔████╔██║      ██╔████╔██║ ██║   ██║  ██║  ██║  ███████╗  ██║   ██║  ██║   ██║  ██║       ███████╗
|  ██║   ██║ ██║╚██╔╝██║  ██  ██║╚██╔╝██║ ██║   ██║  ██║  ██║  ╚════██║  ██║   ██║  ██║   ██║  ██║       ╚════██║     
|  ╚██████╔╝ ██║ ╚═╝ ██║      ██║ ╚═╝ ██║ ╚██████╔╝  ██████╔╝  ███████║  ╚██████╔╝  ╚██████╔╝  ███████╗  ███████║  
|   ╚═════╝  ╚═╝     ╚═╝      ╚═╝     ╚═╝  ╚═════╝   ╚═════╝   ╚══════╝   ╚═════╝    ╚═════╝   ╚══════╝  ╚══════╝
| by M0ds0uls (https://github.com/m0d4s0uls)
|
|
|
[+]
    """)
    internet_check()
    logging.basicConfig(filename='Om_'+str(datetime.datetime.now())+'.log', encoding='utf-8', level=logging.DEBUG , format='%(asctime)s %(levelname)s %(message)s')
    timer=0
    searchquery=""
    while 1:
        print(Fore.CYAN)
        print("[1] Sheduled Search")
        print("[2] Periodical Search")
        print("[3] Recorded Search")
        print("[4] Live Search")
        print("\n")
        query_type = input("[+] Select your option:\t")
        logging.info("INFO: The option seclected is " + query_type)
        print(Fore.CYAN)
        print(Fore.CYAN)
        print("[a] Username Search + Web Search")
        print("[b] Number Search")
        print("[c] Email Search")
        print("[d] UPI Search")
        print("[e] twitter scrapping")
        print("\n")
        search_type = input("[+] Select your option : \t")
        logging.info("INFO: The search type is " + search_type)
        if search_type!="e":
            searchquery = input("[+] Select query to search:\t")
        if query_type=="1" or query_type=="2":
            timer = input("[+] select the time to search:\t")
            print("\n")
        search_query.omsearcher(query_type,search_type,searchquery,int(timer))

if __name__ == '__main__':
    main()      

