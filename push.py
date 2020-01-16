from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC9a0a93c794ae3e4a93694ddc86660c1f"
# Your Auth Token from twilio.com/console
auth_token  = "cc04c62d6570b2b45af998ab08c278e1"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="whatsapp:+6281224907778",
    from_="whatsapp:+14155238886",
    body="Hello from Python!")

print(message.sid)
