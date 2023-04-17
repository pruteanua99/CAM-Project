import requests
import time


def Offline():
    while True:
        try:
            requests.get('http://www.google.com')
            
            time.sleep(5)

        except requests.ConnectionError:

            break
