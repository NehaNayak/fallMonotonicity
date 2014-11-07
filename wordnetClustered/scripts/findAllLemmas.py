import nltk
import sys
from nltk.corpus import wordnet as wn

Lemmas = set()

for synset in list(wn.all_synsets()):
    for lemma in synset.lemmas():
        Lemmas.add(lemma.name().lower())

for lemma in Lemmas:
    sys.stdout.write(lemma+"\n")
