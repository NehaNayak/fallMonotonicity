import sys
from collections import defaultdict

clustered_token_sense_definition = open(sys.argv[1])
unclustered_token_sense_definition = open(sys.argv[2])

unclusteredDefnSense = {}
unclusteredTokenSense = defaultdict(list)
unclusteredSenseToken = defaultdict(list)

for line in unclustered_token_sense_definition:
    (unc_token, unc_sense, unc_definition) = line.split()
    unclusteredDefnSense[unc_definition] = unc_sense
    unclusteredTokenSense[unc_token].append(unc_sense)
    unclusteredSenseToken[unc_sense].append(unc_token)

def defaultdictListHelper():
    return defaultdict(list)

clusteredSenses = defaultdict(defaultdictListHelper)

for line in clustered_token_sense_definition:
    (clu_token, clu_sense, clu_definition) = line.split()
    clu_definitions = clu_definition.split("_;_")
    for d in clu_definitions:
        try:
            clusteredSenses[clu_token][clu_sense].append(unclusteredDefnSense[d])
        except KeyError:
            trial = map(lambda x : x[0]+"_;_"+x[1], zip(clu_definitions[:-1],clu_definitions[1:]))
            for newD in trial:
                if newD in unclusteredDefnSense.keys():
                        clusteredSenses[clu_token][clu_sense].append(unclusteredDefnSense[newD])

for token in unclusteredTokenSense.keys():
    print token, clusteredSenses[token]
    for clu_sense,unc_senses in clusteredSenses[token].iteritems():
        uncSenseSets = map(lambda x: set(unclusteredSenseToken[x]),unc_senses)
        if len(uncSenseSets)>1 and all(x == uncSenseSets[0] for x in uncSenseSets):
            print "cluster candidate",token, clu_sense
