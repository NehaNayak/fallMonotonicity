import sys
import os

actualLocations = []

output = open("actualLocations.txt",'a')

for line in open(sys.argv[1]):
    os.system('clear')
    (a,b,c) = line.split()
    if b.endswith(".n"):
        sys.stdout.write(line)
        isLocation = raw_input("Is it a location? ")
        if isLocation=="y":
            actualLocations.append(line)

for locationLine in actualLocations:
    output.write(locationLine)
