import sys
import pickle
from collections import defaultdict

LemmaToSenseSynset = defaultdict(list)

for line in sys.stdin:
    (lemma, sense, synset) = line.split()
    LemmaToSenseSynset[lemma].append((sense, synset))

pickle.dump(LemmaToSenseSynset,sys.stdout)
