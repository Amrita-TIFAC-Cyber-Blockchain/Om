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


if os.name == "nt":
    os.system("cls")
    os.system("title H4X-Tools")
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
|  ███╗   ███╗   ██████╗   ██████╗   ███████╗   ██████╗   ██╗   ██╗  ██╗       ███████╗ 
|  ████╗ ████║  ██╔═══██╗  ██╔══██╗  ██╔════╝  ██╔═══██╗  ██║   ██║  ██║       ██╔════╝
|  ██╔████╔██║  ██║   ██║  ██║  ██║  ███████╗  ██║   ██║  ██║   ██║  ██║       ███████╗
|  ██║╚██╔╝██║  ██║   ██║  ██║  ██║  ╚════██║  ██║   ██║  ██║   ██║  ██║       ╚════██║     
|  ██║ ╚═╝ ██║  ╚██████╔╝  ██████╔╝  ███████║  ╚██████╔╝  ╚██████╔╝  ███████╗  ███████║  
|  ╚═╝     ╚═╝   ╚═════╝   ╚═════╝   ╚══════╝   ╚═════╝    ╚═════╝   ╚══════╝  ╚══════╝
| by M0ds0uls (https://github.com/m0d4s0uls)
|
|
|
[+]
    """)
    internet_check()

    while 1:
        print(Fore.CYAN)
        print("[1] Username Search + Web search")
        print("[2] Number search")
        print("[3] Email search")
        print("[4] About")
        print("\n")

        a = input("[+] Select your option : \t")

        if a=="1":
            query = str(input("Search query : \t"))
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

        elif a=="2":
            no = str(input("Enter a phone-number without country code : \t"))
            phonenumber_lookup.Number("+91"+no) 
            target = no
            main_url = 'https://upibankvalidator.com/api/upiValidation?upi='
            upi_ids = ['apl','oksbi','okhdfcbank','sbi','okicici','axisbank','ikwik','pnb','hdfc','idfcbank','okaxis','abfspay','ybl','barodapay','upi','paytm','yapl']

            if len(target) > 9:

                if target.find('@')!=-1:
                    response = requests.post(main_url+target).json()

                    if response['isUpiRegistered']:
                # print('found')
                        # print(Fore.CYAN)
                        print(f"{Fore.BLUE}✅ UPI Holder Name: {response['name']}",f"| UPI platform: {target.partition('@')[2]}")
                    else:
                        # print(Fore.RED)
                        # print('Invalid UPI Not found in',i)
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

        # elif a=="3":

            

        else:
            print(Fore.RED + "Invalid option!")
            time.sleep(1)

if __name__ == '__main__':
    main()      

