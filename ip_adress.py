
#
import socket
import launcher
from colorama import Fore, Back, Style
def get_local_ip():
    launcher.later2()
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    print(Fore.BLUE+"⬇️your ip⬇️ ")
    print(Fore.RED+local_ip,Fore.BLUE+"\n[Press enter]")
    input()
    launcher.later2()
    return local_ip
