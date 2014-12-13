import sys
import pickle

Counts = {}

for line in sys.stdin:
    (word, count) = line.split()
    Counts[word]=int(count)

pickle.dump(Counts,sys.stdout)
