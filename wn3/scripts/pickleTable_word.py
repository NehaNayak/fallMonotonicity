import sys
import pickle

LemmaToIndex = {}

for line in sys.stdin:
    (lemma, index) = line.split()
    LemmaToIndex[lemma]=index

pickle.dump(LemmaToIndex,sys.stdout)
