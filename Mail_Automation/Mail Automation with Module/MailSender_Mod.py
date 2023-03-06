import smtplib 
from os.path import basename
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.utils import formatdate

def Mail_Sender(path,receiver):
    sender = input("Enter your Email_Id : ")
    subject = "Sending Log File Using Automation "
    body = "Following Attachment Contains the Information of Process"

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
        psw = input("Enter Password : ") 
        s.login(sender,psw)
        s.sendmail(sender, receiver, msg.as_string())
        s.quit()

    except Exception as obj:
        print("Error : ",obj)
