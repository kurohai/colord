# Download the Python helper library from twilio.com/docs/python/install
from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
ACCOUNT_SID = "AC1157651630d60bd5b1f4a2c35229273a" 
AUTH_TOKEN = "17c4ee0c124b8c1d6c7fd9c2f9f7c587" 

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
 
call = client.calls.create(
    url="http://kurohai.com/voice.xml",
    to="+12056698902",
    from_="+12055752559",
    method="GET",
    status_callback="https://www.myapp.com/events",
    status_callback_method="POST",
    status_events=["initiated", "ringing", "answered", "completed"],
    record='true',
)

print call.sid
