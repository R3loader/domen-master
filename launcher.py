
import requests
from colorama import Fore, Back, Style
import os
#
import domain_checer
import free_domain
import data_manager
from ddos import ddos
import ping
import ip_adress
import update_launcher

from time import sleep

def module():
      import requests
      from colorama import Fore, Back, Style
      import os
def later():
      print("later...")
      sleep(3)
      print('\n' * 100)
def later2():
      print('\n' * 100)

def launcher():
      while True:
            print(Style.BRIGHT+Fore.RED+"\n             \domen-master/\n\n"+
                  Fore.CYAN+"----------------------------------------------\n"+Fore.LIGHTGREEN_EX+
                  "1 - gui launcher                   7 - your ip \n"
                  "2 - search free domain             8 - clear\n"
                  "3 - domain checer                  9 - info version\n"
                  "4 - ddos (site not have proxy)     10 - update launcher\n"
                  "5 - data manager                   11 - None\n"
                  "6 - ping site                      12 - None\n"+Fore.CYAN+
                  "---------------------------------------------\n"+Fore.LIGHTGREEN_EX+
                  "99 - exit       "+Style.BRIGHT+Fore.YELLOW+"By:R3loader "+Fore.GREEN+"     100 - links\n")

            metod = input(Style.BRIGHT+Fore.RED+'Enter metod>> '+Fore.RESET )
            if metod=="1":
                  os.system("python3 gui/main.py ")
            elif metod=="2":
                  later()
            elif metod=="3":
                  later2()
                  domain_checer.free_domain()
            elif metod=="4":
                  later2()
                  ddos()
            elif metod=="5":
                  later2()
                  data_manager.datamanager()
            elif metod=="6":
                  ping.ping()
            elif metod=="7":
                  ip_adress.get_local_ip()
            elif metod=="8":
                  later2()
            elif metod=="9":
                  later2()
                  print("version 0.01\n")
            elif metod=="10":
                  later2()
                  print(Fore.CYAN+"\n1 - download modules\n2 - update\n")
                  update_launcher_metod = input(Style.BRIGHT+Fore.RED+">> ")
                  print(Fore.YELLOW + "")
                  if update_launcher_metod=="1":
                        update_launcher.download()
                  elif update_launcher_metod=="2":
                        update_launcher.update()
                  else:
                        print("\nWhat?\n")
            elif metod=="99":
                  print("\n" * 100)
                  print(Style.BRIGHT+"bye <3"+Fore.RESET+"")
                  exit(232)
            elif metod=="100":
                  later2()
                  print(Style.BRIGHT+Fore.YELLOW+"⬇️github⬇️\n"+Style.BRIGHT+Fore.BLUE+"https://github.com/R3loader/domen-master\n")
            else:
                  print("\nWhat?\n")



