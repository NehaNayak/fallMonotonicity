import sys
import nltk
from nltk.corpus import wordnet as wn

for line in sys.stdin:
    lemma = line[:-1]
    synsets = wn.synsets(lemma)
    if len(synsets)>31:
        ratio = 31.0/len(synsets)
        for pos in ['n','v','a','r']:
            thisPOSSynsets = wn.synsets(lemma,pos)
            limit = ratio*len(thisPOSSynsets)
    
            for index, synset in enumerate(thisPOSSynsets[:int(limit)]):
                sys.stdout.write(\
                "\t".join([\
                lemma,\
                str(index+1),\
                synset.name(),\
                synset.definition(),\
                ])+"\n"\
                )
    else:
        for index, synset in enumerate(synsets):
            sys.stdout.write(\
                "\t".join([\
                lemma,\
                str(index+1),\
                synset.name(),\
                synset.definition(),\
                ])+"\n"\
                )
