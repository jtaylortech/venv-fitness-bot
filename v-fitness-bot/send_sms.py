from twilio.rest import Client


account_sid = "AC3cd750be70538d033d43c5ed21fc1f5e"
auth_token  = "59df6f787d374a02226fb1b412ed81de"
client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+13143983570",
    from_="+18596517102",
    body="lock back in")

print(message.sid)