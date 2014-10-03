import sys
from collections import defaultdict

def defaultdictHelper():
	return defaultdict(list)

FILE_placePairs = open(sys.argv[1],'r')

placePairs = set()

for line in FILE_placePairs:
	(meronym, holonym) = line.split()
	placePairs.add((meronym, holonym))

counts = defaultdict(defaultdictHelper)

people = set()
places = set()

for line in sys.stdin:
	(pattern, place, person) = line.split()
	people.add(person)
	places.add(place)
	counts[pattern][person].append(place)


for k,v in counts.iteritems():
	for k2,v2 in v.iteritems():
		if len(v2)>1:
			for place1 in v2:
				for place2 in v2:
					if (place1,place2) in placePairs:	
						print k, k2, place1, place2
