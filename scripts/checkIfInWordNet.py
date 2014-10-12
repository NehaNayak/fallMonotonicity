import sys
import nltk
from nltk.corpus import wordnet as wn

for line in sys.stdin:
	word = line[:-1]
	x = wn.synsets(word,pos=wn.NOUN)
	if len(x)==0:
		sys.stdout.write(line)

