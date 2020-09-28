import smtplib
import pandas as pd
import csv
import ssl
from email.mime.text import MIMEText
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import sys

sender_email = "%s" %(sys.argv[2])   #Add your email
sender_name = "%s" %(sys.argv[1])
password = "gvxf jvkg htlh xbhb"    #Add your password

#Add csv file name/path
e = pd.read_csv("%s" %(sys.argv[4]))
receiver_emails = e['email'].values
receiver_names =  e["name"].values
print(len(e.index))

for receiver_email, receiver_name in zip(receiver_emails, receiver_names):

    print("Sending to " + receiver_name)
    msg = MIMEMultipart()
    msg['Subject'] = "%s" %(sys.argv[3])
    msg['From'] = formataddr((sender_name, sender_email))
    msg['To'] = formataddr((receiver_name, receiver_email))

    msg.attach(MIMEText("""<h2>Hello, """ + receiver_name  , 'html'))


    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        context = ssl.create_default_context()
        server.starttls(context=context)
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        print('Email sent!')
    except Exception as e:
        print(f'Oh no! Something bad happened!n{e}')
        continue
        
    finally:
        # print('Closing the server...')
        server.quit()