import requests
import time
from recognition.recognition import recunoastere
from geolocation.location import getLocationDetails
from comunication.mail import send_email
from snapShoting import Pozare


def Offline():

    while True:
        try:
            requests.get('http://www.google.com')
            # verificare ip curent
            print('Conexiune la internet detectată.')

            Pozare()
            if not recunoastere():
                send_email(r"D:\NASA\CAM_p\win.png", getLocationDetails())

            # trimitere pe email poza + locatie estimativa
            break

        except requests.ConnectionError:
            print('Nu s-a detectat o conexiune la internet.')
            time.sleep(5)
