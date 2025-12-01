import smtplib

# list of email_id to send the mail
li = ["craftzon25@gmail.com", "vivekkariya22@gmail.com"]

for dest in li:
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("craftzon25@gmail.com", "rougwpmqpgnadzsp")
    message = "Message_you_need_to_send"
    s.sendmail("craftzon25@gmail.com", dest, message)
    s.quit()
