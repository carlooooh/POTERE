import os
import numpy as np
import nltk
import preprocessor as p
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
import scipy
from scipy import spatial
import re

tokenizer = p.ToktokTokenizer()
stopword_list = nltk.corpus.stopwords.words('english')



#pulizia del files testuale
def remove_stopwords(text, is_lower_case=False):
    pattern = r'[^a-zA-z0-9s]'
    text = re.sub(pattern," ",''.join(text))
    tokens = tokenizer.tokenize(text)
    tokens = [tok.strip() for tok in tokens]
    if is_lower_case:
        cleaned_token = [tok for tok in tokens if tok not in stopword_list]
    else:
        cleaned_tokens = [tok for tok in tokens if tok.lower() not in stopword_list]
    filtered_text = ' '.join(cleaned_tokens)
    return filtered_text


#Pulizia dei dati
testo_pulito = []
for file in os.listdir("path/to/directory"):
    if file.endswith(".txt"):
        with open(os.path.join("path/to/directory", file), "r") as f:
            text = f.read()
            testo_pulito.append(remove_stopwords(text))

