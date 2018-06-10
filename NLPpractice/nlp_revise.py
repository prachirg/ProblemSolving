import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import abc, stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import PunktSentenceTokenizer
from nltk.corpus import wordnet
from collections import Counter


cor = abc.raw("rural.txt").lower()
cor_abc = abc.raw("rural.txt").lower()
cor_word_tokens = word_tokenize(cor)
#print(cor_word_tokens)
cor_sent_tokens = sent_tokenize(cor)
#print(cor_sent_tokens)

#stop words
stp = stopwords.words("english")
#print(stp)
filtered_sentence = [i for i in cor_word_tokens if i not in stp and len(i)>2]

# for i in cor_word_tokens:
#      if i not in stp:
#          filtered_sentence.append(i)
#print(filtered_sentence)

#stemming
def filteredstem(input):
    ps = PorterStemmer()
    for w in input:
        print(ps.stem(w))

example_text = ['This', 'is','python','for', 'pythoner', 'doing', 'pythoning']
#filteredstem(example_text)

#POS

custom_sent_tokenizer  = PunktSentenceTokenizer(cor)
tokenized = custom_sent_tokenizer.tokenize(cor_abc)

def process_events():
    for i in tokenized:
        words = nltk.word_tokenize(i)
        tagged = nltk.pos_tag(words)
        entity = nltk.ne_chunk(tagged)
        print(tagged)

#process_events()

#Lemmatizing
wnl = WordNetLemmatizer()
#print(wnl.lemmatize("better",'a'))

#wordnet - synonyms and antonyms

#synonyms
syns = wordnet.synsets("good")
#print(syns)

for i in range(0,len(syns)):
    #print(i)
    syn = syns[i].name()
    #print("synset",syn)
    #word = syns[i].lemmas()[i].name()
    #print("just the word",word)
    deff = syns[i].definition()
    #print(deff)
    ex = syns[i].examples()
    #print(ex)

synoyms = []
antonyms = []

for s in syns:
    for l in s.lemmas():
        synoyms.append(l.name())
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())

#print(set(synoyms))
#print(set(antonyms))
w1 = wordnet.synsets("ship")
w2 = wordnet.synsets("hair")
#print((w1[0].wup_similarity(w2[0]))*100)

#n-grams and count occurences

grams = set(nltk.ngrams(cor_word_tokens,2))
frequency = Counter(grams)


print(frequency)





















