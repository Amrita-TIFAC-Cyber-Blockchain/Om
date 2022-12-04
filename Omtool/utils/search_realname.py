import requests
import random
from utils.randomuser import users
from colorama import Fore


def linkedin(name):
    url = "https://linkedin.com/in/" + name.replace(" ", "-")
    r = requests.get(url)
    r.headers = random.choice(users)
    if r.status_code == 200:
        print(f"{Fore.GREEN}[*] Name found in Linkedin!")
        print(url + "\n")
    else:
        print(Fore.RED + "Unkown USERNAME! \n" + Fore.RESET)


def facebook(name):
    url = "https://facebook.com/" + name.replace(" ", ".")
    r = requests.get(url)
    r.headers = random.choice(users)
    if r.status_code == 200:
        print(f"{Fore.GREEN}[*] Name found in Facebook!")
        print(url + "\n")
    else:
        print(Fore.RED + "Unkown USERNAME!  \n" + Fore.RESET)


def whitepages(name):
    url = "https://whitepages.com/name/" + name.replace(" ", "-")
    r = requests.get(url)
    r.headers = random.choice(users)
    if r.status_code == 200:
        print(f"{Fore.GREEN}[*] Name found in Whitepages!")
        print(url + "\n")
    else:
        print(Fore.RED + "Unkown USERNAME!  \n" + Fore.RESET)


def peoplefinders(name):
    url = "https://peoplefinders.com/name/" + name.replace(" ", "-")
    r = requests.get(url)
    r.headers = random.choice(users)
    if r.status_code == 200:
        print(f"{Fore.GREEN}[*] Name found in Peoplefinders!")
        print(url + "\n")
    else:
        print(Fore.RED + "Unkown USERNAME! \n" + Fore.RESET)