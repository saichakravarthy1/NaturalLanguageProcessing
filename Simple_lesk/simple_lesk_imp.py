from nltk.corpus import wordnet as wn
from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer

wl = WordNetLemmatizer()

sentence = raw_input("Enter the sentence:")
word = raw_input("Enter the word:")

def get_signature(sense):
    set_of_words = []
    defn=wn.synsets(word)[sense].definition()
    exmpl=wn.synsets(word)[sense].examples()
    for i in range(len(exmpl)):
        set_of_words += word_tokenize(exmpl[i])
    set_of_words += word_tokenize(defn)
    signature = [wl.lemmatize(i) for i in set_of_words]
    return signature

def compute_overlay(context,signature):
    overlap = 0
    for cn in context:
        for sn in signature:
            if cn == sn:
                overlap +=1
    return overlap


def lesk(sentence, word):
     
    best_sense= wn.synsets(word,pos = 'n')[0]
    max_overlap=0
    context = word_tokenize(sentence)
    context = [wl.lemmatize(i) for i in context]
    for sense in range(len(wn.synsets(word))):
        signature = get_signature(sense)
        overlap= compute_overlay(context, signature)
        if overlap > max_overlap:
            max_overlap = overlap
            best_sense = wn.synsets(word, pos = 'n')[sense]
    return best_sense

output = lesk(sentence,word)
print output
print output.definition()