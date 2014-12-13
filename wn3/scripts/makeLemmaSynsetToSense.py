import sys
import pickle
from collections import defaultdict

LemmaSynsetToSense = {}

for line in sys.stdin:
    (lemma, sense, synset) = line.split()
    LemmaSynsetToSense[(lemma,synset)]=sense

pickle.dump(LemmaSynsetToSense,sys.stdout)
