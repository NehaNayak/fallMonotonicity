import sys
import nltk
from nltk.corpus import wordnet as wn

WNFormatConvert = {}

for line in sys.stdin:
    (lemma, sense, synset) = line.split()
    WNFormatConvert[synset+"."+lemma] = (lemma,sense) 

Synsets = list(wn.all_synsets())
Lemmas = set()

for synset in Synsets:
    for lemma in synset.lemmas():
        Lemmas.add(lemma)

for lemma in Lemmas:
    antonyms = lemma.antonyms()
    if len(antonyms)>0:
        try:
            (lemma1, sense1) = WNFormatConvert[lemma.__repr__().split("'")[1].lower()]
            for antonym in antonyms:
                (lemma2, sense2) = WNFormatConvert[antonym.__repr__().split("'")[1].lower()]
                sys.stdout.write("\t".join([\
                    lemma1, sense1, lemma2, sense2])+"\n")

        except KeyError:
            pass
