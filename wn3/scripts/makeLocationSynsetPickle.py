import sys
import pickle

LocationSenses = {}

for line in sys.stdin:
    (location, synset) = line.split()
    LocationSenses[location]=synset

pickle.dump(LocationSenses,sys.stdout)
