import smtplib 
from os.path import basename
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.utils import formatdate
import json

def Mail_Sender(path,receiver):
    with open("Credentials.json") as data_file:
        data = json.load(data_file)

        sender = data['Email-ID']
        pwd = data['password']
        
    subject = "Duplicate_File_Removal_Automation"
    body = "Log_File Contains information of All desired output"

    msg = MIMEMultipart()

    msg["Sender"] = sender
    msg["To"] = receiver
    msg["Subject"] = subject
    msg["Date"] = formatdate(localtime = True)

    msg.attach(MIMEText(body))

    fd = open(path,'rb')
    part = MIMEApplication(fd.read())
    Name = basename(path)

    part["Content-Disposition"] = 'attachment; filename = "%s"' %basename(path)

    msg.attach(part)


    try:
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(sender,pwd)
        s.sendmail(sender, receiver, msg.as_string())
        s.quit()

    except Exception as obj:
        print("Error : ",obj)
