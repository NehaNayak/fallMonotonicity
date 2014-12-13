import sys
import pickle

LemmaSynsetToSense = pickle.load(open(sys.argv[1],'r'))

for line in sys.stdin:
    (location, synset) = line.split()
    sys.stdout.write("\t".join([\
        location,LemmaSynsetToSense[(location,synset)]])+"\n")
