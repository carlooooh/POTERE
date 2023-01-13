import os
import numpy as np
import nltk
nltk.download('punkt')
import preprocessor as p
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize, ToktokTokenizer
import scipy
from scipy import spatial
import re

tokenizer = ToktokTokenizer()
stopword_list = nltk.corpus.stopwords.words('english')
test="I'am Carlo and i will save the univers"

query = input("testiamo--> ")


#pulizia del files testuale
def remove_stopwords(text, is_lower_case=False):
    pattern = r'[^a-zA-z0-9s]'
    text = re.sub(pattern," ",''.join(text))
    tokens = tokenizer.tokenize(text)
    tokens = [tok.strip() for tok in tokens]
    if is_lower_case:
        #per evoluzioni future
        cleaned_token = [tok for tok in tokens if tok not in stopword_list]
    else:
        cleaned_tokens = [tok for tok in tokens if tok.lower() not in stopword_list]
    filtered_text = ' '.join(cleaned_tokens)
    return filtered_text



#Inizializzazione dei dati
testo_pulito = []
for file in os.listdir("./NAPOLEONE/"):
    if file.endswith(".txt"):
        with open(os.path.join("./NAPOLEONE/", file), "r") as f:
            text = f.read()
            testo_pulito.append(remove_stopwords(text))

#abbiamo memorizzato, in una lista vuota, tutto il contenuto dei file.txt 'puliti'. Ogni documento viene separato da una ','


#Implementazione corporamento di parole utilizzando un vettore pre-addestrato
glove_vectors = dict()
file = open('glove.6B.50d.txt', encoding = 'utf-8')
for line in file:
    values = line.split()
    word = values[0]
    vectors = np.asarray(values[1:])
    glove_vectors[word] = vectors
file.close()


vec_dimension = 50

# Stiamo creando una funzione che prende una frase e restituisce il vettore di caratteristiche di 300 dimensioni.
def get_embedding(x):
    arr  = np.zeros(vec_dimension)
    text2 = str(x).split()
    for t in text2:
        try:
            vec = glove_vectors.get(t).astype(float)
            arr = arr + vec
        except:
            pass
    arr = arr.reshape(1,-1)[0]
    return(arr/len(text2))


#media di tutti i vettori
out_dict = {}
for doc in testo_pulito:
    frasi = sent_tokenize(doc)
    for frase in frasi:
        average_vector = (np.mean(np.array([get_embedding(x) for x in nltk.word_tokenize(frase)]), axis=0))
        dict = { frase : (average_vector) }
        out_dict.update(dict)
        
        
#print(out_dict)


#Se la funzione restituisce un valore vicino all'1 la frase inserita e il documento hanno un significato simile
#altrimenti se il valore restituito e' vicino lo 0 hanno un significato diverso
def get_sim(query_embedding, average_vector_doc):
    sim = [(1 - scipy.spatial.distance.cosine(query_embedding, average_vector_doc))]
    return sim


def Ranked_documents(query):
    query_words = (np.mean(np.array([get_embedding(x) for x in nltk.word_tokenize(query.lower())],dtype=float), axis=0))
    rank = []
    for k,v in out_dict.items():
        rank.append((k, get_sim(query_words,v)))
        rank = sorted(rank,key=lambda t: t[1], reverse=True)
    print('Ranked Documents :')
    return rank[0]


print(Ranked_documents(query))
