import psycopg2
from collections import defaultdict
import pickle
import sys

def main():    

    mapToIDs = pickle.load(open(sys.argv[1],'r'))

    try:
        conn = psycopg2.connect(database="kbp", user="nayakne", host="jonsson.stanford.edu", port="4242")

    except:
        print "I am unable to connect to the database"
    
    cur = conn.cursor()
    

    for line in sys.stdin:
	(place,path,person) = line.split()
	try:
		sentenceid = mapToIDs[(place,path,person)]
		cur.execute("""SELECT text FROM sentence WHERE sentence_id = '"""+sentenceid+"""'; """)
		text = cur.fetchone()[0][:-1].replace('\n','\\n')
		sys.stdout.write("\t".join([place,path,person,text])+"\n")
	except KeyError:
		pass 
    conn.close()

if __name__ == '__main__':
        main()

