import sys
import pickle

triggerDict = {}

for line in sys.stdin:
	(place, dep1, verb, dep2, person, sentence) = line.split()
	triggerDict[(place.lower(), dep1+"="+verb+"="+dep2, person.lower())] = sentence

pickle.dump(triggerDict,sys.stdout)	
