import nltk
from nltk.corpus import wordnet as wn

adverbsWithHypernymy = []
adverbsWithoutHypernymy = []

for synset in list(wn.all_synsets('r')):
    if not len(synset.hypernyms())==0 or not len(synset.hyponyms())==0:
        adverbsWithHypernymy.append(synset)
    else:
        adverbsWithoutHypernymy.append(synset)
    

print "Number of adverb synsets with hypernymy", len(adverbsWithHypernymy)
print "Number of adverb synsets without hypernymy", len(adverbsWithoutHypernymy)
