import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv() 

TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.environ.get("TWILIO_PHONE_NUMBER")
MY_PHONE_NUMBER = os.environ.get("MY_PHONE_NUMBER")

# It is a best practice to check if the variables were loaded successfully.
if not all([TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE_NUMBER, MY_PHONE_NUMBER]):
    print("Error: One or more required environment variables are missing.")
    print("Please check your .env file and ensure it is in the same directory.")
    exit()

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

try:
    message = client.messages.create(
        to=MY_PHONE_NUMBER,
        from_=TWILIO_PHONE_NUMBER,
        body="Wuvbb You!"
    )
    print(f"Message sent successfully! SID: {message.sid}")
except Exception as e:
    print(f"Failed to send SMS: {e}")