import requests
import time

def Online(functie):

    while True:
        try:
            requests.get('http://www.google.com')
            #verificare ip curent
            print('Conexiune la internet detectată.')

            functie()
            #trimitere pe email poza + locatie estimativa 
            break

        except requests.ConnectionError:
            print('Nu s-a detectat o conexiune la internet.')
            time.sleep(5)


