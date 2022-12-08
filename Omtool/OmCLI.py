# -*- coding: utf-8 -*-

'''
Om - OSINT me 

To perform individual search using unique identifiers like Phone Number, Usernames, Email IDs and 
UPI address.

This is specifically customized for TN Police Hackathon 2022.

Tool Developed by Team ModSouls, TIFAC-CORE in Cyber Security, Amrita Vishwa Vidyapeetham, Coimbatore.

'''

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
from subtools import omuser_search, omupi_search


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

    while 1:
        print(Fore.CYAN)
        print("[1] Sheduled Search")
        print("[2] Periodical Search")
        print("[3] Recorded Search")
        print("[4] Live Search")
        print("\n")
        b = input("[+] Select your option:\t")
        if b=="1":
            print(Fore.CYAN)
            print("[a] Username Search + Web Search")
            print("[b] Number Search")
            print("[c] Email Search")
            print("[d] UPI Search")
            print("[e] Image Search")
            print("[f] About")
            print("\n")
            a = input("[+] Select your option : \t")
            b= input("[+] Select query to search:\t")
            c=input("[+] select the day to search:\t")
            print("\n")
        if b=="2":
            print(Fore.CYAN)
            print("[a] Username Search + Web Search")
            print("[b] Number Search")
            print("[c] Email Search")
            print("[d] UPI Search")
            print("[e] Image Search")
            print("[f] About")
            print("\n")
            a = input("[+] Select your option : \t")
            b= input("[+] Select query to search:\t")
            c=input("[+] select the frequency time to search:\t")
            print("\n")
        if b=="3":
            print(Fore.CYAN)
            print("[a] Username Search + Web Search")
            print("[b] Number Search")
            print("[c] Email Search")
            print("[d] UPI Search")
            print("[e] Image Search")
            print("[f] About")
            print("\n")
            a = input("[+] Select your option : \t")
            b= input("[+] Select query to search:\t")
            print("\n")
            print("Taking the input from DB....")
            print("\n")
        if b=="4":
            while 1:
                print(Fore.CYAN)
                print("[a] Username Search + Web Search")
                print("[b] Number Search")
                print("[c] Email Search")
                print("[d] UPI Search")
                print("[e] Image Search")
                print("[f] About")
                print("\n")

                a = input("[+] Select your option : \t")

                if a=="a":
                    omuser_search.omuser_search();

                elif a=="b":
                    no = str(input("Enter a phone-number: \t"))
                    phonenumber_lookup.Number("+91 " + no) 
                    omupi_search.omupi_search(no);
                elif a=="c":
                    email= input("Enter email to search without @XXX.com:\t")
                    omupi_search.omupi_search(email);
                elif a=="d":
                    upi=input("Enter UPI or number without @xxx:\t")
                    omupi_search.omupi_search(upi);
                else:
                    print(Fore.RED + "Invalid option!")
                    time.sleep(1)

if __name__ == '__main__':
    main()      

