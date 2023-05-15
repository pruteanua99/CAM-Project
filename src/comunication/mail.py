import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
import os


def search_file(filename, directory):
    for root, dirs, files in os.walk(directory):
        if filename in files:
            return os.path.abspath(os.path.join(root, filename))

    return None


def send_email(denumire_img, locatie):

    sender = "cristinacoroi930@gmail.com"
    password = "klipdoteyqklxkqf"
    subject = 'AVERTIZARE FURT LAPTOP!'
    em = MIMEMultipart()
    em['From'] = sender
    em['To'] = sender
    em['Subject'] = subject
    em.attach(MIMEText(f"{locatie}"))
    with open(f"{denumire_img}", "rb") as f:
        file = MIMEImage(f.read(), "jpg")
    em.attach(file)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(sender, password)
        smtp.sendmail(sender, "pruteanualexandru99@yahoo.com", em.as_string())


def main():
    denumire_img = input("denumire_img>")
    location = input("location>")
    send_email(denumire_img, location)


if __name__ == '__main__':
    main()
