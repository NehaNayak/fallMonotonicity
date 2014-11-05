import sys

DefinitionMap = pickle.load(open(sys.argv[1],'r'))

for line in sys.stdin:
    (synset, definition) = line.split()
    definitions = definition.split("_;_")
    for definition in definitions:
        sys.stdout.write(synset+"\t"+DefinitionMap[definition]+"\n")
