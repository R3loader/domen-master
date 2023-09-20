
import requests
import data
from colorama import Fore, Back, Style



def free_domain():
    while True:
        print(Fore.CYAN+"\nBig search"
              "\n1 - format google"
              "\nlink search"
              "\n2 - format "+Fore.BLUE+"https://www.google.com/"+Fore.CYAN+
              "\n"
              "\n99 - exit"
              "\n")
        metod = input(Style.BRIGHT + Fore.RED + 'Enter metod>> ' +Fore.RESET)
        site_name = input(Style.BRIGHT + Fore.RED + 'Site name>> ' +Fore.RESET)
        if metod=="1":
            print(Fore.BLUE+"domens types \n"
                  "1 - none \n"
                  "2 - www\n"
                  "3 - ru")
            domen_types=input(Style.BRIGHT+Fore.RED+'Enter metod>> '+Fore.RESET )
            for domen in data.domens:
                if domen_types == "1":
                    site = f'https://.{site_name}{domen}/'
                    print(site)
                elif domen_types=="2":
                    site = f'https://www.{site_name}{domen}/'
                    print(site)
                elif domen_types=="3":
                    site = f'https://ru.{site_name}{domen}/'
                    print(site)
                else:
                    print("\nWhat?\n")
                try:
                    response = requests.get(site)
                    print(Fore.GREEN+'\nYou can go to the site', site)
                except:
                    print(Fore.RED+'\nYou can not go to the site', site)
        elif metod=="2":
            try:
                response = requests.get(site_name)
                print(Fore.GREEN+'\nYou can go to the site ', site_name)
            except:
                print(Fore.RED+'\nYou can not go to the site ',site_name)
        elif metod=="99":
            break
        else:
            print("\nWhat?\n")


