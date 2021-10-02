# -*- coding: utf-8 -*-
import random
from flask import Flask, request
from pymessenger.bot import Bot
from chat import chatbot

app = Flask(__name__)
ACCESS_TOKEN = 'EAARv9VcVoLQBAM3qFqgVDQX7woAqKdfeNExw5C9HpPCbJ0vEJZAF26Wvq8bmcOMVLZAVzgZCrwHrdyJLDZCZAiEnx3r0IDqnCHuei8GrGDjFCgHpk3gW0c6Lre64a2kVv0F73o6XSREZAkPI3jRZCmxyUmKyLKRq7uxtHNG52dqZCsp3tKhRJjAZC'
VERIFY_TOKEN = 'oLQBABekcGrQ'
APP_SECRET_CODE ='aee409b621257bf42f0aa2e6e8f8a093'
bot = Bot(ACCESS_TOKEN)

#Nous recevrons des messages que Facebook envoie à notre bot à ce point de terminaison 
@app.route("/", methods=['GET', 'POST'])

def webhook():
    if request.method == 'GET':
        token_sent = request.args.get("hub.verify_token")
        return verify_fb_token(token_sent)
    else:
        # obtenir le message qu'un utilisateur a envoyé au bot
       output = request.get_json()
       for event in output['entry']:
          messaging = event['messaging']
          for message in messaging:
            if message.get('message'):
                #Identifiant Facebook Messenger pour l'utilisateur afin 
                # que nous sachions où renvoyer la réponse
                recipient_id = message['sender']['id']
                if message['message'].get('text'):
                    msg_user=message['message']['text']
                    response_sent_text= chatbot(msg_user)
                    send_message(recipient_id, response_sent_text)
                    #si l'utilisateur nous envoie un GIF, une photo, 
                    # une vidéo ou tout autre élément non textuel
                if message['message'].get('attachments'):
                    response_sent_nontext = chatbot(msg_user)
                    send_message(recipient_id, response_sent_nontext)
    return "Message Processed"


def verify_fb_token(token_sent):
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return 'Jeton de vérification non valide'

def send_message(recipient_id, response):
    bot.send_text_message(recipient_id, response)
    return "success"

if __name__ == "__main__":
    app.run()
