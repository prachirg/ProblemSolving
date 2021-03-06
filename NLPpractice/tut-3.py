#Stemming
#Take the root - stem of the word. Eg. riding --> ride

from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()

# example_text = ['python','pythoner','pythoned','pythoning','pythonly']
#
# for w in example_text:
#     print(ps.stem(w))

new_text = "It is very important to be pythonly while you are pythoning with python. All pythoners have pythoned atleast once"

words = word_tokenize(new_text)

for w in words:
    print(ps.stem(w))
