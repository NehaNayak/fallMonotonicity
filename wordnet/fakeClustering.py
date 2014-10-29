import nltk
from nltk.corpus import wordnet as wn
from collections import defaultdict
import sys

def squash(senses,extent=1,limit=31):

    originalSenses=list(senses)

    # Maps to hypernyms, or hyperhypernyms, or whatever
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
    latestHyperSense = -1 # OMG what is this shame on you
    for hyperSense in hyperSenses:
        if latestHyperSense is -1 or not hyperSense[1] == latestHyperSense:
            latestHyperSense = hyperSense[1]
            newSenses.append(hyperSense[0])
    if len(newSenses)<=limit:
        return newSenses
    else:
        return squash(newSenses,extent+1,limit)

def main():

    senseMap = defaultdict(list)

    # Read in token to synset mapping
    for line in sys.stdin:
        (token, senseNum, synset) = line.split()
        senseMap[token].append(wn.synset(synset))

    # Ensmallen the sense lists
    for token, senses in senseMap.iteritems():
        # If there are fewer senses, we can handle it
        if len(senses)>31:
            adverbSenses = filter(lambda x: '.r.' in x.name(),senses)
            nonAdverbSenses = filter(lambda x: '.r.' not in x.name(),senses)
            senseMap[token] = squash(nonAdverbSenses,extent=1,limit=31-len(adverbSenses))+adverbSenses
        # Print out new map to synsets 
        for senseNum, synset in enumerate(senseMap[token]):
            sys.stdout.write(token+"\t"+str(senseNum+1)+"\t"+synset.name()+"\n")

if __name__=="__main__":
    main()
