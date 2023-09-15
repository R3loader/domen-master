
import socket
from colorama import Fore, Back, Style
def ping():
    print("\n"*100)
    print(Fore.MAGENTA+"format - www.google.com \n"
          "99 - exit\n")
    while True:
        ping_name = input(Style.BRIGHT+Fore.RED+'Enter metod>> '+Fore.RESET)
        if ping_name=="99":
            print("\n"*100)
        print(Style.BRIGHT+Fore.GREEN+ping_name,"->",socket.gethostbyname(ping_name),"\n\n")
