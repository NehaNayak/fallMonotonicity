import sys
from collections import defaultdict

Indicators = [\
"a_country_in",\
"a_country_on",\
"a_republic_in",\
"a_republic_on",\
"a_city_in",\
"a_city_of",\
"a_state_in",\
"town_in",\
"town_of",\
"kingdom_in",\
"county_in",\
"county_of",\
"a_borough_of",\
"capital_of",\
"capital_city_of",\
"capital_and_largest_city_of",\
"capital_and_largest_city_in",\
"capital_and_chief_port_of",\
"capital_and_chief_port_in",\
"the_capital_and_largest_city",\
"the_largest_city_in",\
"the_largest_city_of",\
"a_landlocked_country",\
"a_landlocked_republic",\
"a_seaport_on",\
"a_seaport_in",\
"a_port_city_on",\
"a_port_city_in",\
"a_port_in",\
"a_village_in",\
"a_village_on",\
"an_industrial_city",\
"a_constitutional_monarchy",\
"a_monarchy_in",\
"a_monarchy_on",\
"a_province_in",\
"a_province_on",\
"an_ancient_town"\
]

NonIndicators =[\
"mountain_",\
"a_sea_",\
"an_inland_sea",\
"river",\
"lake_in_"\
]

tokenToSenses = defaultdict(list)
locationSenses = open(sys.argv[1],'w')
ambiguousSenses = open(sys.argv[2],'w')

for line in sys.stdin:
    (token, sense, definition) = line.split()
    definitions = definition.split("_;_")
    
    if sense.endswith(".n"):
        for (index,d) in enumerate(definitions):
            tokenToSenses[token].append((d,sense+str(index)))

for token, senses in tokenToSenses.iteritems():
    for sense in senses:
        if any(indicator in sense[0] for indicator in Indicators):
            locationSenses.write(token+"\t"+sense[1]+".l\t"+sense[0]+"\n")
        elif not any(nonIndicator in sense[0] for nonIndicator in NonIndicators):
            ambiguousSenses.write(token+"\t"+sense[1]+"\t"+sense[0]+"\n")
