from flask import Flask, request, redirect
import twilio.twiml
from twilio.rest import TwilioRestClient

app = Flask(__name__)
account = "AC5d445f607cca27580dbb3c540564183c"
token = "d2030dec6833d622609f9d4dc6c4bf9d"
client = TwilioRestClient(account, token)
demo_from = "+16697219918"

@app.route("/", methods=['GET', 'POST'])
def demo():
    from_number = str(request.values.get('From', None))
    from_number = from_number[1:]
    from_number = int(from_number)
    last_digit = from_number % 10

    msg = "Cats cats cats"
    if last_digit < 3:
        msg = "Welcome to FiveStars, the rewards program of Viztango Cafe. Reply \"YES\" to add a free bonus point!"
    elif last_digit < 6:
        msg = "Congrats! You just earned 2 points at Viztango Cafe. You're 6 points away from a free sandwich!"
    else:
        msg = "We haven't seen you around for a while...we miss you! Come in this week and get 20% off your order."

    resp = twilio.twiml.Response()
    resp.message(msg)
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
