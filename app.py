from flask import Flask,request
from twilio.twiml.messaging_response import MessagingResponse
import re
import random

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"

@app.route('/bot', methods=['POST'])
def bot():
    if request.method == 'POST':
        incoming_msg = request.values.get('Body', '')
        # incoming_msg = request.json.get('Body', '')
        response = map_incoming_msg(incoming_msg)

        # create Twilio XML response
        resp = MessagingResponse()
        msg = resp.message()
        msg.body(response)
    
    return str(resp)


@app.route('/email', methods=['POST'])
def email_extractor():
    incoming_msg = request.json.get('Body')
    email_matches = re.findall(r'[\w\.-]+@[\w\.-]+',incoming_msg) 
    return {"email_matches":email_matches}   

def map_incoming_msg(text):
    greeting = {'input':['hi','hello','hey','Wassup'],'output':['Aur bc kya chal rha','Chutiye kuch karle']}
    default_text = 'Kya bol raha bhosdike'
    if text in greeting['input']:
        output_list = greeting['output'] 
        length = len(output_list)   
        return output_list[random.randint(0,length-1)]
    return default_text

if __name__ == "__main__":
    app.run(host='localhost', port=5000,debug=True)
