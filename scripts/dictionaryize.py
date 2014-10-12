import sys
import pickle

triggerDict = {}

for line in sys.stdin:
	(place, dep1, verb, dep2, person, sentence) = line.split()
	triggerDict[(place, dep1+"="+verb+"="+dep2, person)] = sentence

pickle.dump(triggerDict,sys.stdout)	
