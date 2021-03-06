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

data = [
	"baap ke lavde"                         ,
	"chodu"                                 ,
	"chodoo"                                ,
	"choodu"                                ,
	"gandu"                                 ,
	"gaandu"                                ,
	"gandoo"                                ,
	"bhosad"                                ,
	"bhosada"                               ,
	"bhosadaa"                              ,
	"bhosadaaa"                             ,
	"bhosadii"                              ,
	"bhosadika"                             ,
	"bhosadike"                             ,
	"bhosadiki"                             ,
	"bosadike"                              ,
	"bakrichod"                             ,
	"balatkaar"                             ,
	"behen ke laude"                        ,
	"betichod"                              ,
	"bhai chhod"                            ,
	"bhayee chod"                           ,
	"bhen chhod"                            ,
	"bhaynchod"                             ,
	"behanchod"                             ,
	"behenchod"                             ,
	"bhen ke lode"                          ,
	"bhosdi"                                ,
	"bhosdike"                              ,
	"chipkai ki choot ke paseene"           ,
	"cha cha chod"                          ,
	"chod ke bal ka kida"                   ,
	"chopre he randi"                       ,
	"chudasi"                               ,
	"chut ka maindak"                       ,
	"chutia"                                ,
	"chutiya"                               ,
	"chootia"                               ,
	"chutiye"                               ,
	"dheeli choot"                          ,
	"choot"                                 ,
	"chootiya"                              ,
	"gaand chaat mera"                      ,
	"gaand"                                 ,
	"gaand ka khadda"                       ,
	"gaand ke dhakan"                       ,
	"gaand mein kida"                       ,
	"gandi chut mein sadta hua ganda kida"  ,
	"gandmasti"                             ,
	"jhaat ke baal"                         ,
	"jhat lahergaya"                        ,
	"jhatoo"                                ,
	"jhantu"                                ,
	"kukarchod"                             ,
	"kutha sala"                            ,
	"kuthta buraanahe kandaa nahi pattaahe" ,
	"lode jesi shakal ke"                   ,
	"lode ke baal"                          ,
	"lund khajoor"                          ,
	"lund chuse"                            ,
	"lund"                                  ,
	"luhnd"                                 ,
	"lundh"                                 ,
	"madar chod"                            ,
	"maadarchod"                            ,
	"maadar"                                ,
	"madar"                                 ,
	"chod"                                  ,
	"madarchod"                             ,
	"madarchod ke aulaad"                   ,
	"mader chod"                            ,
	"mai chod"                              ,
	"mera mume le"                          ,
	"mere fudi kha ley"                     ,
	"meri ghand ka baal"                    ,
	"randi"                                 ,
	"randi ka choda"                        ,
	"suzit"                                 ,
	"sust lund ki padaish"                  ,
	"tatti ander lele"                      ,
	"tere baap ki gaand"                    ,
	"teri chute mai chuglee"                ,
	"teri gaand mein haathi ka lund"        ,
	"teri maa ki choot"                     ,
	"teri maa ki sukhi bhos"                ,
	"teri phuphi ki choot mein"             ,
	"teri bhosri mein aag"                  ,
	"teri gaand me danda"                   ,
	"teri ma ki choot me bara sa land"      ,
	"teri ma ki chudaye bandar se hui"      ,
	"teri ma randi"                         ,
	"teri maa ke bable"                     ,
	"teri maa ke bhosade ke baal"           ,
	"tu tera maa ka lauda"                  ,
	"amma ki chut"                          ,
	"bhaand me jaao"                        ,
	"bhadva"                                ,
	"bhadve"                                ,
	"chodika"                               ,
	"bhadwe ki nasal"                       ,
	"bhen ke lode maa chuda"                ,
	"bhosad chod"                           ,
	"bhosadchod"                            ,
	"bhosadi ke"                            ,
	"bhosdee kay"                           ,
	"bhosdi k"                              ,
	"bulle ke baal"                         ,
	"bursungha"                             ,
	"camina"                                ,
	"chod bhangra"                          ,
	"choot k bhoot"                         ,
	"choot k pakode"                        ,
	"choot ka paani"                        ,
	"choot ka pissu"                        ,
	"choot ki jhilli"                       ,
	"chudpagal"                             ,
	"chut ke makkhan"                       ,
	"chootiye"                              ,
	"gaand maar bhen chod"                  ,
	"gand mein louda"                       ,
	"gandi fuddi ki gandi auladd"           ,
	"haram zaadaa"                          ,
	"harami"                                ,
	"jhaat"                                 ,
	"kaala lund"                            ,
	"kaali kutti"                           ,
	"kuthri"                                ,
	"kutte"                                 ,
	"kutte ki olad"                         ,
	"lavde ka baal"                         ,
	"lavde"                                 ,
	"lodu"                                  ,
	"lowde ka bal"                          ,
	"lund k laddu"                          ,
	"lund mera muh tera"                    ,
	"maa-cho"                               ,
	"maal chhodna"                          ,
	"mahder chod"                           ,
	"mera gota moo may lay"                 ,
	"mome ka pasina chat"                   ,
	"moo may lay mera"                      ,
	"padosi ki aulaad"                      ,
	"rand ki moot"                          ,
	"randi baj"                             ,
	"randi ka larka"                        ,
	"randi ke bacche"                       ,
	"randi ke beej"                         ,
	"saale lm"                              ,
	"sab ka lund teri ma ki chut mein"      ,
	"sinak se paida hua"                    ,
	"suvar chod"                            ,
	"suwar ki aulad"                        ,
	"tera gittha"                           ,
	"tere maa ka bur"                       ,
	"teri behen ka bhosda faadu"            ,
	"teri gand mai ghadhe ka lund"          ,
	"teri ma bahar chud rahi he"            ,
	"teri ma ko kutta chode"                ,
	"teri maa ka bhosra"                    ,
	"teri maa ka boba chusu"                ,
	"teri maa ki choot me kutte ka lavda"   ,
	"teri maa ki chut"                      ,
	"teri maa ki chute"                     ,
	"tuzya aaichi kanda puchi"              ,
	"bhadavya"                              ,
	"bhikaar"                               ,
	"bulli"                                 ,
	"chinaal"                               ,
	"chut"                                  ,
	"gand"                                  ,
	"maadarbhagat"                          ,
	"chodubhagat"                           ,
	"lundfakir"                             ,
	"gandit"                                ,
	"jhavadya"                              ,
	"laudu"                                 ,
	"lavadya"                               ,
	"muttha"                                ,
	"raandichya"                            ,
	"madarchoth"                            ,
	"benchod"                               ,
	"maadarjaat"                            ,
]

def map_incoming_msg(text):
    # greeting = {'input':['hi','hello','hey','Wassup'],'output':['Aur bc kya chal rha','Chutiye kuch karle']}
    # default_text = 'Kya bol raha bhosdike'
    # if text in greeting['input']:
        # output_list = greeting['output'] 
        # length = len(output_list)   
        # return output_list[random.randint(0,length-1)]
    return str(*random.choices(data))

if __name__ == "__main__":
    app.run(host='localhost', port=5000,debug=True)
