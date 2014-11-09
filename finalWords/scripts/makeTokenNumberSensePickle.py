import pickle
import sys
from collections import defaultdict

TokenNumberToSynset = defaultdict(dict)

for line in sys.stdin:
	(token, number, synset, definition) = line[:-1].split("\t")
	TokenNumberToSynset[token][number]=synset

pickle.dump(TokenNumberToSynset,sys.stdout)
