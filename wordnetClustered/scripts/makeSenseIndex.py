import nltk
from nltk.corpus import wordnet as wn
import sys
from collections import defaultdict

def main():

    for line in sys.stdin:
        (others, gloss) = line.split('|')
        others_separate = others.split(" ")
        synset_offset = others_separate[0]
        ss_type=others_separate[2]
        word = others_separate[4]
        lex_id = "{0:0{1}d}".format(int(others_separate[5],16),2)
        definition = "_".join(gloss.split())

        sys.stdout.write(synset_offset+"."+ss_type+"\t"+definition+"\n")

if __name__=='__main__':
    main()            
