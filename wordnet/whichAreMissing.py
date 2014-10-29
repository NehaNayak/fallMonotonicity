import sys
import nltk
from nltk.corpus import wordnet as wn

for line in sys.stdin:
    s = wn.synset(line[:-1])
    sys.stdout.write(s.name()+"\t"+s.definition()+"\n")
