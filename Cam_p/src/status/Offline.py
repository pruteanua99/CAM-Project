import requests
import time
from recognition.recognition import recognition as r
from geolocation.location import location as loc
from comunication.mail import mailing as m
from snapShoting.pozare import snapshot as s


def Offline():

    while True:
        try:
            requests.get('http://www.google.com')
            # verificare ip curent
            print('Conexiune la internet detectată.')

            s.Pozare()
            if not r.recunoastere():
                m.send_email(r"D:\NASA\CAM_p\win.png",
                             loc.getLocationDetails())

            # trimitere pe email poza + locatie estimativa
            break

        except requests.ConnectionError:
            print('Nu s-a detectat o conexiune la internet.')
            time.sleep(5)
