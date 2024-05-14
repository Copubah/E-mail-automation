from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import smtplib
import os


## Setting up the email addresses
from_address='copubah@gmail.com'
to_address='charlesopuba@gmail.com'
msg=MIMEMultipart()
msg['From']=from_address
msg['To']=",".join(to_address)
msg['subject']='Hi there'

body='This is Charles'
msg.attach(MIMEText(body,'plain'))
email=""
password=""

mail=smtplib.SMTP('smtp.gmail.com', 587)
mail.ehlo()
mail.starttls()
mail.login(email,password)
text=msg.as_string()
mail.sendmail(from_address,to_address,text)
mail.quit()
