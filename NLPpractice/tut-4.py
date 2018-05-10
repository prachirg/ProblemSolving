import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer #unsupervised machine learning tokenizer

train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")

custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

tokenized = custom_sent_tokenizer.tokenize(sample_text)

