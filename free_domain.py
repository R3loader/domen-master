
import requests
import data


from colorama import Fore, Back, Style

def free_domain():
    while True:
        print("")
        metod= input(Style.BRIGHT + Fore.RED + 'Enter metod>> ' +Fore.RESET)
        site_name = input(Style.BRIGHT + Fore.RED + 'Site name>> ' +Fore.RESET)
        if metod=="1":
            print("domens types \n"
                  "1 - none \n"
                  "2 - www"
                  "3 - ru")
            domen_types = int(input(">> "))
            for domen in data.domens:
                if domen_types == 1:
                    site = f'https://.{site_name}{domen}'
                elif domen_types==2:
                    site = f'https://ru.{site_name}{domen}'
                else:
                    site = f'https://www.{site_name}{domen}'
                try:
                    response = requests.get(site)
                    print(f'You can go to the site {site}')
                except:
                    print(f'You can not go to the site {site}')
        elif metod=="2":
            try:
                response = requests.get(site_name)
                print(f'You can go to the site ', site_name)
            except:
                print(f'You can not go to the site ',site_name)
        elif metod=="99":
            break