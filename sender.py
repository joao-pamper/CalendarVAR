import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os
def send_email(link: str):
    load_dotenv()

    SENDER_APP_PASSWORD = os.getenv("SENDER_APP_PASSWORD")
    SENDER_EMAIL = os.getenv("SENDER_EMAIL")
    # Email sender and receiver
    receiver_email = input("Enter the email for the receiver below.\n>")

    # Create the email content
    subject = "Link for your event"
    body = """Hi!\nThank you for using CalendarVAR for creating your event. 
    The link below can be shared with others so that they can add your event to their calendar!
    \n""" + link + """\n \nThank you!\nCalendarVAR"""

    # Create a MIME object
    message = MIMEMultipart()
    message["From"] = SENDER_EMAIL
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    # Connect to the SMTP server and send the email
    print("Sending email...")
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_APP_PASSWORD)
            server.send_message(message)
            print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {e}")
