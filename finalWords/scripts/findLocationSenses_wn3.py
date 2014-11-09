import sys
from collections import defaultdict

Indicators = [\
"a country in",\
"a country on",\
"a republic in",\
"a republic on",\
"a city in",\
"a city of",\
"a state in",\
"town in",\
"town of",\
"kingdom in",\
"county in",\
"county of",\
"a borough of",\
"capital of",\
"capital city of",\
"capital and largest city of",\
"capital and largest city in",\
"capital and chief port of",\
"capital and chief port in",\
"the capital and largest city",\
"the largest city in",\
"the largest city of",\
"a landlocked country",\
"a landlocked republic",\
"a seaport on",\
"a seaport in",\
"a port city on",\
"a port city in",\
"a port in",\
"a village in",\
"a village on",\
"an industrial city",\
"a constitutional monarchy",\
"a monarchy in",\
"a monarchy on",\
"a province in",\
"a province on",\
"an ancient town"\
]

NonIndicators =[\
"mountain ",\
"a sea ",\
"an inland sea",\
"river",\
"lake in "\
]

locationSenses = open(sys.argv[1],'w')
ambiguousSenses = open(sys.argv[2],'w')

for line in sys.stdin:
    (token, sense, definition) = line.split("\t")
    if any(indicator in definition for indicator in Indicators):
        locationSenses.write(token+"\t"+sense+".l\t"+definition)
    elif not any(nonIndicator in sense[0] for nonIndicator in NonIndicators):
        ambiguousSenses.write(token+"\t"+sense+"\t"+definition)
