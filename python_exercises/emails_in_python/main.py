import smtplib
from dotenv import load_dotenv
import os
from email.message import EmailMessage

load_dotenv() # load our env file

SENDER_EMAIL = os.environ.get("MY_EMAIL_ADDRESS")
APP_PASSWORD = os.environ.get("MY_EMAIL_PASSWORD")

email_msg=EmailMessage()
email_msg["from"]="Shubham Pawar"
email_msg["to"]="recipient@local"
email_msg["subject"]="I have Sent you this mail using python -_-"
email_msg.set_content("This is automated Email")

email_msg.add_alternative(f"""
<!DOCTYPE html>
<html>
    <body>
        <h1 style="color:red;">This is Automated Python mail sent to you!</h1>
        <p>Thanks for opening</p>
    </body>
</html>
""", subtype='html')


try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(SENDER_EMAIL, APP_PASSWORD)
        smtp.send_message(email_msg)
        print("Email sent successfully!")
except Exception as e:
    print(f"Failed to send email: {e}")

