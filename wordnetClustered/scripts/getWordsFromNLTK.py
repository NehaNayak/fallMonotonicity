import sys
import nltk
from nltk.corpus import wordnet as wn
import pickle

locations = set(pickle.load(open(sys.argv[1],'r')))
locationSenseFile = open(sys.argv[2],'w')

for synset in list(wn.all_synsets()):
    for lemma in synset.lemmas():
        sys.stdout.write(lemma.name()+"\t"+synset.name()+"\t"+synset.definition()+"\n")
        if "_".join(lemma.name().lower().split()) in locations:
            locationSenseFile.write(lemma.name()+"\t"+synset.name()+"\t"+synset.definition()+"\n")
            
