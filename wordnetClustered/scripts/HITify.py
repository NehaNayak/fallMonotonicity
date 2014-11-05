import sys
import random

def titlecase(inp):
    output = inp[0].upper()+inp[1:]
    return output

Gold = [\
("wurzburg", "gold", "a_city_of_south_central_Germany"),\
("aachen", "gold", "a_city_in_western_Germany_near_the_Dutch_and_Belgian_borders;_formerly_it_was_Charlemagnes_northern_capital"),\
("frederick", "gold", "a_town_in_northern_Maryland_west_of_Baltimore"),\
("des_moines", "gold", "the_capital_and_largest_city_in_Iowa"),\
("quito", "gold", "the_capital_of_Ecuador"),\
("samaria", "gold", "an_ancient_city_in_central_Palestine_founded_in_the_9th_century_BC_as_the_capital_of_the_northern_Hebrew_kingdom_of_Israel;_the_site_is_in_present-day_northwestern_Jordan"),\
("panama", "gold", "a_republic_on_the_Isthmus_of_Panama;_achieved_independence_from_Colombia_in_1903"),\
("castries", "gold", "a_port_on_the_island_of_Saint_Lucia;_capital_and_largest_city_of_Saint_Lucia"),\
("joao_pessoa", "gold", "a_city_in_northeastern_Brazil_near_the_Atlantic_Ocean_north_of_Recife"),\
("philippi", "gold", "a_city_in_ancient_Macedonia_that_was_important_in_early_Christianity"),\
("alpena", "gold", "a_town_in_northern_Michigan_on_an_arm_of_Lake_Huron"),\
("bangkok", "gold", "the_capital_and_largest_city_and_chief_port_of_Thailand;_a_leading_city_in_southeastern_Asia;_noted_for_Buddhist_architecture"),\
("haiphong", "gold", "a_port_city_in_northern_Vietnam;_industrial_center"),\
("biloxi", "gold", "a_old_town_in_southern_Mississippi_on_the_Gulf_of_Mexico"),\
("melbourne", "gold", "the_capital_of_Victoria_state_and_2nd_largest_Australian_city;_a_financial_and_commercial_center"),\
("melbourne", "gold", "a_resort_town_in_east_central_Florida"),\
("spokane", "gold", "a_city_in_eastern_Washington_near_the_Idaho_border"),\
("juarez", "gold", "a_city_in_northern_Mexico_on_the_Rio_Grande_opposite_El_Paso"),\
("wuhan", "gold", "a_city_of_central_China_on_the_Chang_Jiang;_the_commercial_and_industrial_center_of_central_China"),\
("paris", "gold", "the_capital_and_largest_city_of_France;_and_international_center_of_culture_and_commerce"),\
("paris", "gold", "a_town_in_northeastern_Texas"),\
("brownsville", "gold", "a_city_in_southern_Texas_on_the_Rio_Grande_near_its_mouth_into_the_Gulf_of_Mexico;_has_a_channel_that_accommodates_oceangoing_ships"),\
]
Data = []

for line in sys.stdin:
    (location, identifier, definition) = line.split() 
    Data.append((location, identifier, definition))


sys.stdout.write(",".join(["Location"+str(i)+",Definition"+str(i)+",Identifier"+str(i) for i in range(1,11)])+"\n")

for i in range(len(Data)/10):
    x = random.randint(0,9)
    while x>0 and Data[10*i+x-1][0]==Data[10*i+x][0]:
        x-=1
    Data.insert(10*i+x,Gold[i%len(Gold)])

for j in range(len(Data)/10):
    for k in range(10*j,10*j+9):
        sys.stdout.write(titlecase(Data[k][0].replace("_"," "))+",\""+Data[k][2].replace("_"," ")+"\","+Data[k][1]+",")
    k = 10*j+9
    sys.stdout.write(titlecase(Data[k][0].replace("_"," "))+",\""+Data[k][2].replace("_"," ")+"\","+Data[k][1]+"\n")
