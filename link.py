
import requests
import pyshorteners
import data
import launcher


def links():

    def shorten_url(url):
        try:
            response = requests.get(url)
            print('\nYou can go to the site', url)
        except:
            print('\nYou can not go to the site', url)
            print("y/n")
            quest = input("continue?>> ")
            if quest=="y":
                print("Ok...\n")
            elif quest=="n":
                launcher.launcher()
        print("mask link")
        for c in data.url_mask:
            print("\n"+str(c)+url)
        return pyshorteners.Shortener().clckru.short(url)

    url = input("Enter URL: ")
    print("URL Shoter - ", format(shorten_url(url)))
