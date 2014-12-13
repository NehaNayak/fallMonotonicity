import sys

lastSynset = ""
synonyms = []

for line in sys.stdin:
    (lemma, sense, synset) = line.split()
    if not synset==lastSynset:
        if len(synonyms)>1:
            for (lemma1, sense1) in synonyms:
                for (lemma2, sense2) in synonyms:
                    if not lemma1 == lemma2 or not sense1 == sense2:
                        sys.stdout.write("\t".join(\
                            [lemma1,sense1,lemma2,sense2])+"\n")
        lastSynset = synset
        synonyms = [(lemma,sense)]
    else:
        synonyms.append((lemma,sense))
