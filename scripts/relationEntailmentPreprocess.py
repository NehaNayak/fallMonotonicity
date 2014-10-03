import sys
from collections import defaultdict

def defaultdictHelper():
	return defaultdict(list)

FILE_placePairs = open(sys.argv[1],'r')

counts = defaultdict(defaultdictHelper)

people = set()
places = set()

for line in sys.stdin:
	(pattern, place, person) = line.split()
	people.add(person)
	places.add(place)
	counts[place][person].append(pattern)


for k,v in counts.iteritems():
	for k2,v2 in v.iteritems():
		if len(v2)>1:
			for pattern1 in v2:
				for pattern2 in v2:
					if not pattern1 == pattern2:
						print k, k2, pattern1, pattern2	
