import nltk
from nltk.corpus import wordnet as wn
import sys
from collections import defaultdict

def getSynset(dataFile, offset):
    dataFile.seek(offset)
    line = dataFile.readline()

    (others, gloss) = line.split('|')
    others_separate = others.split(" ")

    offset = others_separate[0]
    ss_type=others_separate[2]

    return offset+"."+ss_type

def main():

    dataFile = open(sys.argv[1],'r')

    for line in sys.stdin:
        splitLine = line.split()
        (lemma, pos, synset_cnt, p_cnt) = splitLine[0:4]    
        synsets = splitLine[4+int(p_cnt)+2:]
        for synset in synsets:
            sys.stdout.write(lemma+"\t"+getSynset(dataFile,int(synset))+"\n")

if __name__=='__main__':
    main()            
