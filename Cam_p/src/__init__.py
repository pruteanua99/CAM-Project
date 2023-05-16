import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sys
sys.path.append('./src')
# sys.path.append('D:\NASA\ProiectAvionV2\.venv\Lib\site-packages')
sys.path.append('src')


sender_email = "sender@yahoo.com"
receiver_email = "receiver@example.com"
password = "your_password"
