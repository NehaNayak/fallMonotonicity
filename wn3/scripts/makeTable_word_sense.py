import sys
import pickle

for line in sys.stdin:
    (lemma, sense, synset, defn) = line[:-1].split("\t")
    sys.stdout.write("\t".join([\
            lemma,\
            sense,\
            defn])+"\n")
