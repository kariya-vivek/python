import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Sender and receiver details
sender_email = "craftzon25@gmail.com"
receiver_email = "vivekkariya22@gmail.com"
password = "rougwpmqpgnadzsp"

# Create the email
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = "Test Email from Python"

# Email body
body = "Hello! This is a test email sent from a Python script."
message.attach(MIMEText(body, "plain"))

# Connect to Gmail SMTP server and send email
try:
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()  # Secure the connection
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        print("Email sent successfully!")
except Exception as e:
    print(f"Error: {e}")
