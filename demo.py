from flask import Flask, request, redirect
import twilio.twiml
from twilio.rest import TwilioRestClient

app = Flask(__name__)
account = "AC5d445f607cca27580dbb3c540564183c"
token = "d2030dec6833d622609f9d4dc6c4bf9d"
client = TwilioRestClient(account, token)
demo_from = "+16697219918"

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond to incoming calls with a simple text message."""

    resp = twilio.twiml.Response()
    resp.message("Hello, Mobile Monkey")
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)



# message = client.messages.create(to="+14088215768", from_=demo_from,
#                                  body="Hello there!")