import sys
import nltk
from nltk.corpus import wordnet as wn
from collections import defaultdict

TokenNumberToSynset = {}
TopLemmas = defaultdict(dict)

for line in sys.stdin:
    (token, number, synset, definition) = line[:-1].split("\t")
    pos = synset.split(".")[-2]
    TokenNumberToSynset[(token,number)]=synset
    if wn.synset(synset).lemmas()[0].name().lower()==token:
        TopLemmas[synset][pos]=(token,number)

for (token,number), synset in TokenNumberToSynset.iteritems():
    pos = synset.split(".")[-2]
    for hypernym in wn.synset(synset).hypernyms():
        try:
            topLemma = TopLemmas[hypernym.name()][pos]
            sys.stdout.write(\
                "\t".join([\
                token,\
                number,\
                topLemma[0],\
                topLemma[1],\
                "0\n"
                ])\
                )
            sys.stdout.write(\
                "\t".join([\
                topLemma[0],\
                topLemma[1],\
                token,\
                number,\
                "1\n"
                ])\
                )
        except:
            print "aaaaaaah",hypernym 
