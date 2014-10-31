import sys

synset_definition = open(sys.argv[1],'r')
token_synset = open(sys.argv[2],'r')

synsetDefinition = {}

for line in synset_definition:
    (synset,definition) = line.split()
    synsetDefinition[synset] = definition

for line in token_synset:
    (token, synset) = line.split()
    sys.stdout.write(token+"\t"+synset+"\t"+synsetDefinition[synset]+"\n")
