
import requests
import data




def free_domain():
    while True:
        print("\nBig search"
              "\n1 - format google"
              "\nlink search"
              "\n2 - format https://www.google.com/"
              "\n"
              "\n99 - exit"
              "\n")
        metod = input(">> ")
        site_name = input("Name site>> ")
        if metod=="1":
            print("domens types \n"
                  "1 - none \n"
                  "2 - www\n"
                  "3 - ru")
            domen_types = input(">> ")
            for domen in data.domens:
                if domen_types == "1":
                    site = f'https://.{site_name}{domen}'
                    print(site)
                elif domen_types=="2":
                    site = f'https://www.{site_name}{domen}'
                    print(site)
                elif domen_types=="3":
                    site = f'https://ru.{site_name}{domen}'
                    print(site)
                else:
                    print("\nWhat?\n")
                try:
                    response = requests.get(site_name)
                    print('\nYou can go to the site', site_name)
                except:
                    print('\nYou can not go to the site', site_name)
        elif metod=="2":
            try:
                response = requests.get(site_name)
                print('You can go to the site ', site_name)
            except:
                print('You can not go to the site ',site_name)
        elif metod=="99":
            break
        else:
            print("\nWhat?\n")


