
import smtplib
from email.message import EmailMessage

msg = EmailMessage()
msg.set_content("Test message.")
msg['Subject'] = "Test Subject!!!"
msg['From'] = "ranfge@gmail.com"

email_list = ["samsul71bd@gmail.com", "abc@gmail.com"]


msg['To'] = email_list[0]
server = smtplib.SMTP(host='smtp.gmail.com', port=465)
server.starttls()
server.login("ranfge@gmail.com", "Rana9911@")
server.send_message(msg)
server.quit()
