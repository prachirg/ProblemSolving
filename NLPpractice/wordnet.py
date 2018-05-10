from nltk.corpus import wordnet

#synonym
syns = wordnet.synsets("cake")
syns1 = wordnet.synsets("bar")
print("synsets:",syns)
print("Sysnets-1:",syns1)

#synset
#print(syns[0].name())

#size of synsets
#print(len(syns))

#just the name
#print(syns[3].lemmas()[1].name())
print("lemma:",syns1[7].lemmas())


#definition
print(syns[0].definition())
print(syns1[5].definition())

#similarity
w1 = syns[0]
w2 = syns1[4]
#print(syns[3])
print(w1.wup_similarity(w2))
#print(wu)

