import nltk
from nltk.corpus import wordnet as wn
import sys
from collections import defaultdict

def makeSenseIndex(sense_index_file):
    for synset in list(wn.all_synsets()):
        sense_index_file.write(synset.name()+"\t")
        sense_index_file.write("_".join(synset.definition().split())) 
        sense_index_file.write("\n")

def expand(pos, word):
    expForms = []

    if pos=="noun":
        expForms.append(word+"s")
        if word.endswith("s"):
            expForms.append(word[:-1]+"ses")
        elif word.endswith("x"):
            expForms.append(word[:-1]+"xes")
        elif word.endswith("z"):
            expForms.append(word[:-1]+"zes")
        elif word.endswith("ch"):
            expForms.append(word[:-2]+"ches")
        elif word.endswith("sh"):
            expForms.append(word[:-2]+"shes")
        elif word.endswith("man"):
            expForms.append(word[:-3]+"men")
        elif word.endswith("y"):
            expForms.append(word[:-1]+"ies")
        return expForms

    elif pos=="verb":
        expForms.append(word+"s")
        expForms.append(word+"es")
        expForms.append(word+"ed")
        expForms.append(word+"ing")
        if word.endswith("y"):
            expForms.append(word[:-1]+"ies")
        elif word.endswith("e"):
            expForms.append(word[:-1]+"es")
            expForms.append(word[:-1]+"ed")
            expForms.append(word[:-1]+"ing")
        return expForms

    elif pos=="adj":
        expForms.append(word+"er")
        expForms.append(word+"est")
        if word.endswith("e"):
            expForms.append(word[:-1]+"er")
            expForms.append(word[:-1]+"est")

    return expForms 

def main():

    """ 
    sense_index_file = open(sys.argv[1],'w')
    makeSenseIndex(sense_index_file)
    """
    """ 
    for pos in ['noun','verb','adj']:
        token_input_file = open(pos+"Tokens.txt",'r')
        token_output_file = open(pos+"Tokens_expanded.txt",'w')
        for line in token_input_file:
            expForms = expand(pos,line[:-1])
            token_output_file.write(line)
            for form in set(expForms):
                token_output_file.write(form+"\n")
    """
    """ 
    token_input_file = open("expandedVocab.txt",'r')
    token_output_file = open("token_synset.txt",'w')
    for line in token_input_file:
        synsets = wn.synsets(line[:-1])
        uniqueSynsets = []
        for i in synsets:
            if i not in uniqueSynsets:
                uniqueSynsets.append(i)
        for index, synset in enumerate(uniqueSynsets):
            token_output_file.write(line[:-1]+"\t"+str(index+1)+"\t"+synset.name()+"\n")
    """
    
         
if __name__=='__main__':
    main()
