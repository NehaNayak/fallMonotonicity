import sys
from collections import defaultdict

token_sense_definition = open(sys.argv[1],'r')
locations = open(sys.argv[2],'r')

definitions = defaultdict(list)

for line in token_sense_definition:
    (token, sense, definition) = line.split()
    definitions[token].append(sense+"\t"+definition)

locationSenses = defaultdict(list)

for line in locations:
    try:
        x = definitions[line[:-1]]
	locationSenses[line[:-1]]=x
    except KeyError:
	pass

for location, senses in locationSenses.iteritems():
	for sense in senses:
		sys.stdout.write(location+"\t"+sense+"\n")
