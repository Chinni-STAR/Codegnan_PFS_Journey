import smtplib
from email.message import EmailMessage
sender = "chinnimusirana@gmail.com"
password = "wfiufgilyvsffpzm"
msg = EmailMessage()
msg['Subject'] = "Registration"
msg['From'] = sender
msg['To'] = "ghv0999@gmail.com"
msg.set_content("Registration Successful")
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender, password)
server.send_message(msg)
server.quit()