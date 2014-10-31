import sys
import nltk
from nltk.corpus import wordnet as wn
import pickle
from collections import defaultdict
import unicodedata

countDict = pickle.load(open('cntlist.pickle','r'))

newSynsets = defaultdict(list)

for line in sys.stdin:
    (word, senseNum, synset) = line.split()
    p = wn.synset(synset).lemmas()[0].key().encode('ascii','ignore')
    try:
        count = countDict[p]
        if count > 1:
            newSynsets[word].append(synset)
    except KeyError:
        pass

for word, synsets in newSynsets.iteritems():
    print word+"\t"+str(len(synsets))        
