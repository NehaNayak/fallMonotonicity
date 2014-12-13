import sys
import nltk
from nltk.corpus import wordnet as wn

for line in sys.stdin:
    lemma = line[:-1]
    synsetsOrig = wn.synsets(lemma)
    synsets=[ii for n,ii in enumerate(synsetsOrig) if ii not in synsetsOrig[:n]]
    if len(synsets)>30:
        count = 0
        ratio = 30.0/len(synsets)
        for pos in ['n','v','a','r']:
            thisPOSSynsets = wn.synsets(lemma,pos)
            limit = ratio*len(thisPOSSynsets)
    
            for index, synset in enumerate(thisPOSSynsets[:int(limit)]):
                sys.stdout.write(\
                "\t".join([\
                lemma,\
                str(count+index+2),\
                synset.name(),\
                synset.definition(),\
                ])+"\n"\
                )
            count+=int(limit)
    else:
        for index, synset in enumerate(synsets):
            sys.stdout.write(\
                "\t".join([\
                lemma,\
                str(index+2),\
                synset.name(),\
                synset.definition(),\
                ])+"\n"\
                )
