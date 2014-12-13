import sys
import nltk
from nltk.corpus import wordnet as wn
import pickle

LemmaToSenseSynset = pickle.load(open(sys.argv[1],'r'))

for line in sys.stdin:
    (lemma1, lemma2, cost) = line.split()  

    synsets1 = wn.synsets(lemma1,'v')
    synsets2 = wn.synsets(lemma2,'v')

    for (number1, synset1) in LemmaToSenseSynset[lemma1]:       
        if ".v." in synset1: 
            for (number2, synset2) in LemmaToSenseSynset[lemma2]:       
                if ".v." in synset2:
                    sys.stdout.write("\t".join([\
                        lemma1, number1,\
                        lemma2, number2,
                        cost])+"\n")
