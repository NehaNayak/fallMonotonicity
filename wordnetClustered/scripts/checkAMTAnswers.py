import sys

Answers = {}

for line in sys.stdin:
    (Sense, Answer) = line.split()
    Answers[Sense] = Answer

for line in open(sys.argv[1]):
    try:
        (location, sense, definition) = line.split()
        sys.stdout.write("\t".join([location, definition, Answers[sense]])+"\n")
    except KeyError:
        pass
