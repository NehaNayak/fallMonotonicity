import nltk
from nltk.corpus import wordnet as wn
import sys

for line in sys.stdin:
    synsets = wn.synsets(line[:-1],'n')
    if len(synsets)>1:
        for synset in synsets:
            sys.stdout.write(line[:-1]+"\t"+synset.name()+"\t"+synset.definition()+"\n")
