import socket
import time
from colorama import Fore


class Scan:
    def __init__(self, ip):
        try:
            ip_addr = socket.gethostbyname(ip)
            print(Fore.GREEN + f"[*] Trying to find the IP address of {ip}")
            time.sleep(2)
            print(f"{Fore.GREEN}[*] IP address of the website : \t ", ip_addr)
        except Exception as e:
            print(f"{Fore.RED}[*] Can't connect to the server..!" + Fore.RESET)
            print(f"{Fore.RED}[*] Detailed error : ", e)
