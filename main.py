from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import smtplib
import os


## Setting up the connection server
smtp = smtplib.SMTP('smtp.gmail.com', 587)
smtp.ehlo()
smtp.starttls()
smtp.login('charlesopuba@gmail.com', 'password')

## sending the message

def message(subject="Test",
            text="", img=None,
            attachment=None):
    msg= MIMEMultipart()

    ## SUBJECT
    msg['subject']