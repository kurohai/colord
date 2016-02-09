from twilio.rest import TwilioRestClient
from pprint import pprint

# put your own credentials here 
ACCOUNT_SID = "AC1157651630d60bd5b1f4a2c35229273a" 
AUTH_TOKEN = "17c4ee0c124b8c1d6c7fd9c2f9f7c587" 
 
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 
 
call = client.calls.create(
    to="+12056698902",
    from_="+12055752559",
    method="POST",
    url="http://kurohai.com/voice.xml",
    fallback_method="GET",
    status_callback_method="GET",
    record="true",
    if_machine="Continue",
)

pprint(dir(call))
print call.sid
print call.answered_by
pprint(dir(call.recordings))
