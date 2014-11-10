import math
import sys
import pickle
from collections import defaultdict

def findLCS(Ancestors1, Ancestors2):
	
	LCS=None

	for ancestor in Ancestors1:
		if ancestor in Ancestors2:
			LCS=ancestor

	if LCS==None:
		for ancestor in Ancestors2:
			if ancestor in Ancestors1:
				LCS=ancestor

	return LCS

Ancestor = pickle.load(open(sys.argv[1],'r'))

Counts = defaultdict(int)

for line in sys.stdin:
	(location, frequency) = line.split()
	try:
		for ancestor in Ancestor[location]:
			Counts[location]+=int(frequency)
	except:
		pass

for key in Counts.keys():
	for ancestor in Ancestor[key]:
		try:
			print "==",Counts[findLCS(Ancestor[key],Ancestor[ancestor])]
			print "==",key, Counts[key],ancestor,Counts[ancestor]
            JCD = 2.0*math.log(Counts[findLCS])
			Lin = float(2*math.log(Counts[findLCS(Ancestor[key],Ancestor[ancestor])]))/math.log(Counts[key]*Counts[ancestor])
			sys.stdout.write(key+"\t"+ancestor+"\t"+str(Lin)+"\n")	
		except ValueError:
			pass
		except ZeroDivisionError:
			pass
