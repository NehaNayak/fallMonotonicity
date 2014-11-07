import sys
import random

GoldYes = [
("Namibia", "goldYes", "a republic in southwestern Africa on the south Atlantic coast (formerly called South West Africa); achieved independence from South Africa in 1990; the greater part of Namibia forms part of the high Namibian plateau of South Africa"),
("South_West_Africa", "goldYes", "a republic in southwestern Africa on the south Atlantic coast (formerly called South West Africa); achieved independence from South Africa in 1990; the greater part of Namibia forms part of the high Namibian plateau of South Africa"),
("Windhoek", "goldYes", "capital of Namibia in the center of the country"),
("Herat", "goldYes", "a city in northwestern Afghanistan on the site of several ancient cities"),
("Jalalabad", "goldYes", "a town in eastern Afghanistan (east of Kabul)"),
("Kabul", "goldYes", "the capital and largest city of Afghanistan; located in eastern Afghanistan"),
("Kandahar", "goldYes", "a city in southern Afghanistan; an important trading center"),
("Qandahar", "goldYes", "a city in southern Afghanistan; an important trading center"),
("Albania", "goldYes", "a republic in southeastern Europe on the Adriatic coast of the Balkan Peninsula"),
("Tirana", "goldYes", "the capital and largest city of Albania in the center of the country"),
("Algeria", "goldYes", "a republic in northwestern Africa on the Mediterranean Sea with a population that is predominantly Sunni Muslim; colonized by France in the 19th century but gained autonomy in the early 1960s"),
("Algiers", "goldYes", "an ancient port on the Mediterranean; the capital and largest city of Algeria"),
("Batna", "goldYes", "a town in north central Algeria"),
("Blida", "goldYes", "a city in northern Algeria at the foot of the Atlas Mountains to the southwest of Algiers"),
("Oran", "goldYes", "a port city in northwestern Algeria and the country's 2nd largest city"),
("Djanet", "goldYes", "a desert town in southeastern Algeria"),
("Reggane", "goldYes", "a town in central Algeria"),
("Timgad", "goldYes", "an ancient town founded by the Romans; noted for extensive and well-preserved ruins"),
("Timimoun", "goldYes", "a town in central Algeria in the Atlas Mountains"),
("Angola", "goldYes", "a republic in southwestern Africa on the Atlantic Ocean; achieved independence from Portugal in 1975 and was the scene of civil war until 1990")
]

GoldNo = [
("flora", "goldNo", "(botany) a living organism lacking the power of locomotion"),
("hit", "goldNo", "(baseball) a successful stroke in an athletic contest (especially in baseball)"),
("anchorage", "goldNo", "the act of anchoring"),
("docking", "goldNo", "the act of securing an arriving vessel with ropes"),
("clinch", "goldNo", "(boxing) the act of one boxer holding onto the other to avoid being hit and to rest momentarily"),
("lam", "goldNo", "a rapid escape (as by criminals)"),
("hit", "goldNo", "a conspicuous success"),
("bloomer", "goldNo", "an embarrassing mistake"),
("purchase", "goldNo", "the acquisition of something for payment"),
("assumption", "goldNo", "the act of taking possession of or power over something"),
("assumption", "goldNo", "the act of assuming or taking for granted"),
("conversion", "goldNo", "a spiritual enlightenment causing a person to lead a new life"),
("magic", "goldNo", "an illusory feat; considered magical by naive observers"),
("bender", "goldNo", "a pitch of a baseball that is thrown with spin so that its path curves as it approaches the batter"),
("raise", "goldNo", "the act of raising something"),
("spring", "goldNo", "a light self-propelled movement upwards or forwards"),
("wheeling", "goldNo", "propelling something on wheels"),
("rolling", "goldNo", "propelling something on wheels"),
("hit", "goldNo", "the act of contacting one thing with another"),
("best", "goldNo", "the supreme effort one can make")
]

Data = []

for line in sys.stdin:
    (location, identifier, definition) = line[:-1].split("\t") 
    Data.append((location, identifier, definition))

sys.stdout.write(",".join(["Location"+str(i)+",Definition"+str(i)+",Identifier"+str(i) for i in range(1,21)])+"\n")

for i in range(len(Data)/20):
    x = random.randint(0,18)
    while x>0 and Data[20*i+x-1][0]==Data[20*i+x][0]:
        x-=1
    Data.insert(20*i+x,GoldYes[i%len(GoldYes)])
    x = random.randint(0,19)
    while x>0 and Data[20*i+x-1][0]==Data[20*i+x][0]:
        x-=1
    Data.insert(20*i+x,GoldNo[i%len(GoldNo)])

for j in range(len(Data)/20):
    for k in range(20*j,20*j+19):
        sys.stdout.write(Data[k][0].replace("_"," ")+","+Data[k][2].replace("_"," ")+","+Data[k][1]+",")
    k = 20*j+19
    sys.stdout.write(Data[k][0].replace("_"," ")+","+Data[k][2].replace("_"," ")+","+Data[k][1]+"\n")
