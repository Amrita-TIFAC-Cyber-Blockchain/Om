import json
import time
from urllib.request import urlopen
from colorama import Fore


class Lookup:
    def __init__(self, ip):
        try:
            url = "http://ip-api.com/json/" + ip
            values = json.load(urlopen(url))

            print(Fore.GREEN + f"[*] Trying to find the IP address of {ip}")
            time.sleep(1)
            print(f"{Fore.GREEN}[*] Ip Address - ", values['query'])
            print(f"{Fore.GREEN}[*] Country - ", values['country'])
            print(f"{Fore.GREEN}[*] City - ", values['city'])
            print(f"{Fore.GREEN}[*] ISP - ", values['isp'])
            print(f"{Fore.GREEN}[*] Region - ", values['regionName'])
            print(f"{Fore.GREEN}[*] Timezone - ", values['timezone'])
            print(f"{Fore.GREEN}[*] Zip - ", values['zip'])
            print(f"{Fore.GREEN}[*] Lat - ", values['lat'])
            print(f"{Fore.GREEN}[*] Lon - ", values['lon'])
            print(f"{Fore.GREEN}[*] AS - ", values['as'])

        except Exception as e:
            print(f"{Fore.RED}[*] Can't find any information for the given IP address!" + Fore.RESET)
            print(f"{Fore.RED}[*] Detailed error : ", e)
            return
