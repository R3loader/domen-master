
import socket
import launcher
from colorama import Fore, Back, Style
def ping():
    launcher.later2()
    print(Fore.MAGENTA+"format - www.google.com \n"
          "99 - exit\n")
    while True:
        ping_name = input(Style.BRIGHT+Fore.RED+"ping site>> ")
        if ping_name=="99":
            launcher.later2()
            launcher.launcher()
        print(Style.BRIGHT+Fore.GREEN+ping_name,"->",socket.gethostbyname(ping_name),"\n\n")