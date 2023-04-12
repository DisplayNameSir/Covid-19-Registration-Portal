# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

# Set environment variables for your credentials
# Read more at http://twil.io/secure
account_sid = "AC6e5ddbbc08048c697058226731d6675f"
auth_token = "b6eb2d45015723d2bb8c0b09dd3526f6"
client = Client(account_sid, auth_token)

message = client.messages.create(
  body="Testing",
  from_="+18883016704",
  to="+14086444882"
)

print(message.sid)