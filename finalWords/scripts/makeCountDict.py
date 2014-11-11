import math
import sys
import pickle
from collections import defaultdict

Ancestor = pickle.load(open(sys.argv[1],'r'))
Counts = defaultdict(int)
for line in sys.stdin:
    (word, frequency) = line.split()
    for word_sense in Ancestor.keys():
        if word_sense[0]==word:
            for ancestor in Ancestor[word_sense]:
                Counts[ancestor[0]]+=int(frequency)
pickle.dump(Counts,sys.stdout)
