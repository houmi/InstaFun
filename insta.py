import requests
import urllib


def getUserInfo(url):
    webUrl = urllib.request.urlopen(url)
    print("Result code: " + str(webUrl.getcode()))

def main():
    url = "https://www.instagram.com/instagram"
    getUserInfo(url)

if __name__ == "__main__":
    main()

