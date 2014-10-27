import nltk
from nltk.corpus import wordnet as wn
from collections import defaultdict
import sys

senseMap = defaultdict(list)

def squash(senses,extent=1):
    originalSenses=list(senses)
    for i in range(extent):
        hyperSenses = []
        for sense in senses:
            hypernyms = sense.hypernyms()
            if len(hypernyms)>0:
                hyperSenses.append((sense,hypernyms[0]))
        senses=map(lambda x:x[1],hyperSenses)
    hyperSenses = zip(originalSenses,map(lambda x:x[1],hyperSenses))
    # guaranteed to be stable, thanks Python
    hyperSenses.sort(key = lambda x:x[1])
    newSenses = []
    latestHyperSense = None
    for hyperSense in hyperSenses:
        if latestHyperSense is None or not hyperSense[1] == latestHyperSense:
            latestHyperSense = hyperSense[1]
            newSenses.append(hyperSense[0])
    if len(newSenses)<32:
        return newSenses
    else:
        return squash(newSenses,extent+1)

def main():
    for line in sys.stdin:
        (token, senseNum, synset) = line.split()
        senseMap[token].append(wn.synset(synset))
    for token, senses in senseMap.iteritems():
        if len(senses)>32:
            senseMap[token] = squash(senses)
        for senseNum, synset in enumerate(senseMap[token]):
            sys.stdout.write(token+"\t"+str(senseNum+1)+"\t"+synset.name()+"\n")
if __name__=="__main__":
    main()
