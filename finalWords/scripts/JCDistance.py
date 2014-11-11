import math
import sys
import pickle
from collections import defaultdict

def findLCS(Ancestors1, Ancestors2):
    LCS=None
    for ancestor in Ancestors1:
        if ancestor in Ancestors2:
            LCS=ancestor
    if LCS==None:
        for ancestor in Ancestors2:
            if ancestor in Ancestors1:
                LCS=ancestor
    return LCS

Ancestor = pickle.load(open(sys.argv[1],'r'))
Counts = defaultdict(int)
Words = set()
for line in sys.stdin:
    (word, frequency) = line.split()
    Words.add(word)
    print "-",word
    for word_sense in Ancestor.keys():
        if word_sense[0]==word:
            for ancestor in Ancestor[word_sense]:
                Counts[ancestor[0]]+=int(frequency)

for key in Ancestor.keys():
    try:
        for ancestor in Ancestor[key]:
            LCS = findLCS(Ancestor[key],Ancestor[ancestor])
#            print Counts[key[0]], "c"
            if LCS is not None and Counts[key[0]]>0:
                JCD = 2.0*\
                    math.log(Counts[LCS[0]])-\
                    math.log(Counts[key[0]])-\
                    math.log(Counts[ancestor[0]])    
                sys.stdout.write(key+"\t"+ancestor+"\t"+str(JCD)+"\n")	
    except KeyError:
        print "error",key
