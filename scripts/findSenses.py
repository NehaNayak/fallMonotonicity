import sys
import nltk
from nltk.corpus import wordnet as wn

def printMeronymTree(root):	
		print root.name().split(".")[0] +"\t"+ root.name()
		for meronym in root.part_meronyms():
			printMeronymTree(meronym)

containers = []

for line in sys.stdin:
	word = line[:-1]
	containers.append(word)

for container in containers:
	x = wn.synsets(container,pos=wn.NOUN)
	if len(x)>0:
		printMeronymTree(x[0])
