import nltk
# nltk.download()
#Tokenize

from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
example_text = "Hello Mr. Smith, how are you doing today? The weather is great and python is awesome. The sky is bluish and water is greenish."

print(sent_tokenize(example_text))
tokens = word_tokenize(example_text)
for i in word_tokenize(example_text):
    print(i)

#Part of speech tagging
tagged = nltk.pos_tag(tokens)
print(tagged)

#Stemming
for token in tokens:
    #print("token:",token)
    stemm = nltk.PorterStemmer().stem(token)
    print("stemm:",stemm)

stop_words = set(stopwords.words('English'))
print("stop words:",stop_words)

sentence = [tokens for t in tokens if t in stop_words ]
print(len(sentence))

#Frequency distribution

# fdist1 = FreqDist(example_text)