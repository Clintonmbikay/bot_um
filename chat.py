#encoding UTF-8
import random
import json
import torch


from model import NeuralNet

from spacy_utlis import bag_of_words, tokenize, stem

device = 'cuda' if torch.cuda.is_available() else 'cpu'

with open('intents.json', 'r') as json_data:
    intents = json.load(json_data)

FILE = "data.pth"

data = torch.load(FILE)

input_size = data["input_size"]

hidden_size = data["hidden_size"]

output_size = data["output_size"]

all_words = data['all_words']

tags = data['tags']

model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)

model.load_state_dict(model_state)

model.eval()


def chatbot(sentence):

    bot_name = "Dupond"

    #print("Hello ! Je suis Dupond le Chatbot de UM  Ma mission : vous accompagner dans la découverte de notre université. ")

    while True:

        #sentence = input("Vous: ")

        #if sentence == "Quittez":

            #break

        sentence = tokenize(sentence) 
        
        X = bag_of_words(sentence, all_words)

        X = X.reshape(1, X.shape[0])

        X = torch.from_numpy(X).to(device)

        output = model(X)

        _, predicted = torch.max(output, dim=1)

        tag = tags[predicted.item()]
        probs = torch.softmax(output, dim=1)
        prob = probs[0][predicted.item()]

        if prob.item() > 0.75:

            for intent in intents['intents']:

                if tag == intent["tag"]:
                    return (f"{random.choice(intent['responses'])}")
                    #print(f"{bot_name}: {random.choice(intent['responses'])}")

        else:
            return (f"Je suis désolé mais je n'ai pas compris votre demande.\n Veuillez Réformuler votre démande!")
            #print(f"{bot_name}: Je suis désolé mais je n'ai pas compris votre demande.\n Veuillez Réformuler votre démande!")
