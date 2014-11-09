import pickle
import sys

LocationNumberSynset = pickle.load(open(sys.argv[1],'r'))
LocationsInWordnet_FILE = open(sys.argv[2],'r')
ConfirmedLocations_FILE = open(sys.argv[3],'r')

LocationsInWordnet = {}

for line in LocationsInWordnet_FILE:
	(location, sense) = line.split()
	LocationsInWordnet[location]=sense

for line in ConfirmedLocations_FILE:
	(location, sense, definition) = line[:-1].split("\t")
	LocationsInWordnet[location.lower()]=sense.lower()[:-2]

for line in sys.stdin:
	location = line[:-1]
	if location in LocationsInWordnet.keys():
		flag = False
		for senseNumber, synset in LocationNumberSynset[location].iteritems():
			if synset==LocationsInWordnet[location]:
				sys.stdout.write(location+"\t"+senseNumber+"\n")
				flag=True
		if not flag:
			sys.stdout.write(location+"\t1\n")
	else:
		sys.stdout.write(location+"\t1\n")
