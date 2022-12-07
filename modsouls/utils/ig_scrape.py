from instagram_private_api import Client, ClientCompatPatch
from colorama import Fore
from utils.randomuser import users


class Scrape:
    def __init__(self, target):
        # read username and password from igscrape/username.txt and igscrape/password.txt
        try:
            with open("igscrape/username.txt", "r") as f:
                username = f.read()
            with open("igscrape/password.txt", "r") as f:
                password = f.read()
        except Exception as e:
            print(f"{Fore.RED}[*] Username or password invalid!", Fore.RESET)
            return

        # login to instagram
        try:
            api = Client(username, password)
            data = api.username_info(target)
        except Exception as e:
            print(f"{Fore.RED}[*] Error : ", e, Fore.RESET)
            return

        # print data
        print(f"{Fore.GREEN}----->Scraping data from the account {target}<-----", Fore.RESET)
        print(f"{Fore.GREEN}[*] Username : ", data["user"]["username"])
        print(f"{Fore.GREEN}[*] Full Name : ", data["user"]["full_name"])
        print(f"{Fore.GREEN}[*] Biography : ", data["user"]["biography"])
        print(f"{Fore.GREEN}[*] External Url : ", data["user"]["external_url"])
        print(f"{Fore.GREEN}[*] Followers : ", data["user"]["follower_count"])
        print(f"{Fore.GREEN}[*] Following : ", data["user"]["following_count"])
        print(f"{Fore.GREEN}[*] Is Private : ", data["user"]["is_private"])
        print(f"{Fore.GREEN}[*] Is Verified : ", data["user"]["is_verified"])
        print(f"{Fore.GREEN}[*] Profile Pic Url : ", data["user"]["hd_profile_pic_url_info"]["url"])
        print("Thanks for using modsouls😎")