import smtplib
from email.mime.text import MIMEText

sender = 'admin@example.com'
receivers = ['vinothpreethi16@gmail.com']


port = 1025
msg = MIMEText('This is test mail')

msg['Subject'] = 'Test mail'
msg['From'] = sender
msg['To'] = receivers

with smtplib.SMTP('localhost', port) as server:
    
    # server.login('username', 'password')
    server.sendmail(sender, receivers, msg.as_string())
    print("Successfully sent email")