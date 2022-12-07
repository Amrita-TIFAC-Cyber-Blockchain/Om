import phonenumbers as p
from phonenumbers import geocoder
from phonenumbers import carrier
from colorama import Fore


class Number:
    def __init__(self, no):
        print("\n")
        try:
            ph_no = p.parse(no)
            geo_location = geocoder.description_for_number(ph_no, 'en')
            no_carrier = carrier.name_for_number(ph_no, 'en')
            # liste=time_zones_for_number(ph_no)
            print(f"{Fore.YELLOW}[*] Country : \t", geo_location)
            print(f"{Fore.YELLOW}[*] Sim Provider \t: ", no_carrier)
            # print(colored.green("[+]Time Zone:"+str(liste[0])))
        except Exception:
            print(f"{Fore.RED}No data were found for this number!" + Fore.RESET)
