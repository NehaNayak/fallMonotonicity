import math
import sys
from collections import defaultdict

def cosine(vec1,vec2):
    Num = sum(map(lambda x:x[0]*x[1],zip(vec1,vec2)))
    Den1 =  math.sqrt(sum(map(lambda x:x**2,vec1)))
    Den2 =  math.sqrt(sum(map(lambda x:x**2,vec2)))
    return Num/(Den1*Den2)

Vectors = {}

for line in sys.stdin:
    thisLine = line.split()
    word = thisLine[0]
    Vectors[word]= map(lambda x: float(x), thisLine[1:])

for word1, vec1 in Vectors.iteritems():
    Distances = [(cosine(vec1, vec2),word2) for word2, vec2 in Vectors.iteritems()]
    Distances = sorted(Distances)[-100:]
    Distances.reverse()
    for x in Distances:
        sys.stdout.write("\t".join([word1,x[1],str(x[0])])+"\n")       
    

