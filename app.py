from flask import Flask,request
from twilio.twiml.messaging_response import MessagingResponse
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"

@app.route('/bot', methods=['POST'])
def bot():
    response ='test karatani'
    print(request.method)
    if request.method == 'POST':
        incoming_msg = request.values.get('Body', '')

        # create Twilio XML response
        resp = MessagingResponse()
        msg = resp.message()
        response = "*Hi! I am the Quarantine Bot*"
        msg.body(response)
    
    return str(response)

if __name__ == "__main__":
    app.run(host='localhost', port=5000)
