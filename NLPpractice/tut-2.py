#stop words
# words like a, the, and, of  .. etc.
# these words are filler words and not useful for analytics

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example_sent="This is an example showing stop words filteration"
stop_words = set(stopwords.words("English"))
print(len(stop_words))

words= word_tokenize(example_sent)
#filter_sentence = []

# for w in words:
#     if w not in stop_words:
#         filter_sentence.append(w)
# print(filter_sentence)

filter_sentence=[w for w in words if w not in stop_words]



print(filter_sentence)



