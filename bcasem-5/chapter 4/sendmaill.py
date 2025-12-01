import smtplib
import ssl
from email.message import EmailMessage

# --- Configuration ---
sender_email = "craftzon25@gmail.com"  # Replace with your email address
password = "rougwpmqpgnadzsp"         # Replace with your App Password
receiver_email = "vivekkariya22@gmail.com" # Replace with recipient's email

# Create a secure SSL context
ssl_context = ssl.create_default_context()

# --- Build the email message ---
message = EmailMessage()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = "Simple Email from Python"
message.set_content("This is the body of the email. It was sent using smtplib.")

# --- Sending the email ---
try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=ssl_context) as server:
        # Log in to the server
        server.login(sender_email, password)

        # Send the email
        server.send_message(message)

    print("Email sent successfully!")

except Exception as e:
    print(f"An error occurred: {e}")
