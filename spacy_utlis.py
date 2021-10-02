import numpy as np
import spacy

nlp= spacy.load('fr_core_news_sm')

def tokenize(sentence):

    """
    diviser la phrase en un éventail de mots/jetons
    un jeton peut être un mot ou un caractère de ponctuation, ou un nombre

    """
    docx= nlp(sentence)
    token_array =[]
    for token in docx:
        token_array.append(token.text)
    return token_array

def stem(word):

    """
    stemming = trouver la forme racine du mot
    Exemples:
    mots = ["organiser », « organise », « organiser"]
    mots = [stem(w) pour w en mots]
    -> ["orgue », « orgue », « orgue"]

    """
    docx = nlp(word.lower())
    return docx[0].lemma_

def bag_of_words(tokenized_sentence, words):

    """

    bag de retour de tableau de mots:
    1 pour chaque mot connu qui existe dans la phrase, 0 autrement
    exemple:
    phrase = ["bonjour », « comment », « sont », « vous"]
    mots = ["salut », « bonjour », « je », « vous », « bye », « merci », « cool"]
    tourbière = [ 0 , 1 , 0 , 1 , 0 , 0 , 0 ]

    """

    sentence_words = [stem(word) for word in tokenized_sentence]

    # initialiser bag avec 0 pour chaque mot

    bag = np.zeros(len(words), dtype=np.float32)

    for idx, w in enumerate(words):

        if w in sentence_words: 

            bag[idx] = 1


    return bag
