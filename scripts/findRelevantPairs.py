import sys

placesThatAppear= set()

placesAppearingFile = open(sys.argv[1],'r')

for line in placesAppearingFile:
	placesThatAppear.add(line[:-1])

for line in sys.stdin:
	(meronym, holonym) = line.split()
	if meronym in placesThatAppear and holonym in placesThatAppear:
		print meronym,holonym

