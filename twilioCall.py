from twilio.rest import Client

account = ""
token = ""
client = Client(account, token)

call = client.calls.create(to="number to call",
                           from_="+12029294075",
                           url="http://twimlets.com/holdmusic?Bucket=com.twilio.music.ambient")
print(call.sid)
