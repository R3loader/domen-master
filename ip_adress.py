
#
import socket
from colorama import Fore, Back, Style
def get_local_ip():
    print("\n" * 100)
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    print(Fore.BLUE+"⬇️your ip⬇️ ")
    print(Fore.RED+local_ip,Fore.BLUE+"\n[Press enter]")
    input()
    print("\n" * 100)
    return local_ip
