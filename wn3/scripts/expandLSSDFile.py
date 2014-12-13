import sys
from collections import defaultdict
import pickle

Locations = pickle.load(open(sys.argv[1],'r'))

for line in sys.stdin:
    locationLemma = line[:-1]
    if locationLemma not in Locations.keys():
        sys.stdout.write("\t".join([\
            locationLemma, "1", "_location", "location"])+"\n")
