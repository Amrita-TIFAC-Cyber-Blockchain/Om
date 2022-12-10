from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
import smtplib


message = MIMEMultipart()
message["from"] = "modsouls@gmail.com"
message["to"] = "vinothpreethi16@gmail.com"
message["subject"] = "test"
message.attach(MIMEText("Body"))
message.attach(MIMEImage(Path("Image")))

with smtplib.SMTP(host="smtp.gmail.com",port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("Username","Password")
    smtp.send_message(message)
    print("Sent...")