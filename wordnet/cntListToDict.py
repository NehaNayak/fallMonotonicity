import nltk
import pickle
from nltk.corpus import wordnet as wn
import sys

Counts = {}

for line in sys.stdin:
    (freq, key, senseNum) = line.split()
    Counts[key] = freq

pickle.dump(Counts,sys.stdout)
