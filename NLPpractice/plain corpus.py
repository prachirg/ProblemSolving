import nltk
from nltk.corpus import abc, stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from collections import Counter
from nltk.stem import PorterStemmer
from nltk import ngrams
from nltk.tokenize import PunktSentenceTokenizer

print(abc.fileids())
#_tokenize(abc.raw("rural.txt"))))

def practice():
    stemmed_tokens = []
    train_tokens = word_tokenize(abc.raw("rural.txt").lower())
    bigrams = list(ngrams(train_tokens,3))
    POS_tag = nltk.pos_tag(train_tokens)
    print(POS_tag)
    #custom_tokenizer = PunktSentenceTokenizer(train_tokens)
    #word_token = custom_tokenizer.tokenize(sample_tokens)
    ps = PorterStemmer()
    for token in train_tokens:
        stemmed_value = ps.stem(token)
        stemmed_tokens.append(stemmed_value)

    frequencies = Counter(stemmed_tokens)
    stop_words = stopwords.words('English')

    for word, count in frequencies.most_common(50):
        if word not in stop_words and len(word) > 2:
            #continue

            print(word,count)
    #print(words_not_in_stop_words)

    #print(all_tokens)

        #print(stemmed_tokens,count)
practice()



