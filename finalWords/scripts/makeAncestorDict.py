import sys
import pickle
from collections import defaultdict

Parent = defaultdict(list)
Ancestor = defaultdict(list)

def getParents(key,Parent):
	returnList = []
	try:
		nextParents = Parent[key]
		returnList+=nextParents
		for parent in nextParents:
			returnList+=getParents(parent,Parent)
	except KeyError:
		pass
	return returnList
	
Words = set()

for line in sys.stdin:
    (Word1, Sense1, Word2, Sense2) = line.split()
    w1 = (Word1,Sense1)
    w2 = (Word2,Sense2)
    Parent[w1].append(w2)
    Words.add(w1)
    Words.add(w2)

Parent = dict(Parent)

for key in Words:
    Ancestor[key].append(key)
    Ancestor[key]+=getParents(key,Parent)

pickle.dump(dict(Ancestor),open(sys.argv[1],'w'))
