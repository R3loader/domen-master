import os


def launch():
    print("1 - no module laucher\n"
          "2 - module laucher\n")
    sel_metod_lauhch = input(" >>")
    if sel_metod_lauhch=="1":
        no_module_launcher()
    elif sel_metod_lauhch=="2":
        colorama_launcher()
    else:
        print("\nWhat?\n")
def download():
    os.system("python.exe -m pip install --upgrade pip")
    os.system("pip3 install requests colorama")
def update():
    os.system("python.exe -m pip install --upgrade pip")
    os.system("pip3 uninstall requests colorama")
    os.system("pip3 install requests colorama")
def colorama_launcher():
    from colorama import Fore, Back, Style
    import launcher
    launcher.later2()
    print(Fore.CYAN + "\n1 - download modules\n2 - update\n99 - exit\n")
    update_launcher_metod = input(Style.BRIGHT + Fore.RED + 'Enter metod>> ' +Fore.RESET)
    print(Fore.YELLOW + "")
    if update_launcher_metod == "1":
        download()
    elif update_launcher_metod == "2":
        update()
    elif update_launcher_metod == "3":
        exit()
    elif update_launcher_metod=="3":
        print("Your os?\n1 - windows\n2 - linux")
        update_launcher_metod_os = input(">> ")
        if update_launcher_metod_os=="1":
            os.system("python.exe -m pip install --upgrade pip")
        elif update_launcher_metod_os=="2":
            print("update python3")
            os.system("sudo apt-get update python3")
            print("pip upgrate...")
            os.system("python3 pip install --upgrade pip")
    else:
        print("\nWhat?\n")
def no_module_launcher():
    print("\n1 - download modules\n2 - update\n3 - update pip-python")
    update_launcher_metod = input(">> ")
    if update_launcher_metod=="1":
        download()
    elif update_launcher_metod=="2":
        update()
    elif update_launcher_metod=="3":
        print(Fore.YELLOW+"Your os?\n1 - windows\n2 - linux")
        update_launcher_metod_os = input(">> ")
        if update_launcher_metod_os=="1":
            os.system("python.exe -m pip install --upgrade pip")
        elif update_launcher_metod_os=="2":
            print("update python3")
            os.system("sudo apt-get update python3")
            print("pip upgrate...")
            os.system("python3 pip install --upgrade pip")
