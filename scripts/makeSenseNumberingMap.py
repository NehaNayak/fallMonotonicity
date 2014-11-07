import sys
from collections import defaultdict
import pickle

SenseMap = defaultdict(dict())

for line in sys.stdin:
    (token, number, synset, definition) = line.split()
    SenseMap[token][number] = synset
