import os


def download():
    os.system("python.exe -m pip install --upgrade pip")
    os.system("pip3 install requests colorama")
def update():
    os.system("python.exe -m pip install --upgrade pip")
    os.system("pip3 uninstall requests colorama")
    os.system("pip3 install requests colorama")