
import data
from time import sleep
import launcher
import os
#
def datamanager():
    while True:
        print("1 - directory\n2 - data.py\n99 - exit\n")
        metod = input(Style.BRIGHT + Fore.RED + 'Enter metod>> ' + Style.RESET_ALL + Fore.RESET_ALL)
        if metod=="1":
            print(os.path.dirname(os.path.abspath(__file__)))
        elif metod=="2" :
            print("⬇️available domains⬇️ ")
            print(data.domens,"\n[Press enter]")
            input()
            launcher.later2()
        elif metod=="99":
            break
        else:
            print("\nWhat?\n")