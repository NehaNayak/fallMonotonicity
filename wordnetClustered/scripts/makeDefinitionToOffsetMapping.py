import sys

for line in sys.stdin:
    (others, gloss) = line.split('|')
    sys.stdout.write("_".join(gloss.split()))
    sys.stdout.write("\t"+others.split()[0]+"\n")
