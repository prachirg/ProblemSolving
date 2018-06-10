
from nltk.corpus import names
from nltk.classify import NaiveBayesClassifier

#data preparation
data = ([(name,"male") for name in names.words("male.txt")] + [(name, "female") for name in names.words("female.txt")])

#feature extraction
def feature_gender(word):
    return {'last letter': word[-1]}

feature = [(feature_gender(n),g) for (n,g) in data] 



#train and predict

train_sets = feature
classifier = NaiveBayesClassifier.train(train_sets)
print(classifier.classify(feature_gender('Prachi')))

