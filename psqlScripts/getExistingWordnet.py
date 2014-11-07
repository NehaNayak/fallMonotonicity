import psycopg2
from collections import defaultdict
import pickle
import sys

def main():    
    try:
        conn = psycopg2.connect(database="naturalli", user="nayakne", host="jonsson", port="5432")

    except:
        print "I am unable to connect to the database"
    
    cur = conn.cursor()
    

    for line in sys.stdin:
	try:
		cur.execute("""\
            SELECT wso.gloss, e.source_sense, wsi.gloss, e.sink_sense\
            FROM word wso, word wsi, edge e\
            WHERE e.source=wso.index and e.sink=wsi.index\
            LIMIT 2""")
		text = cur.fetchone()[0][:-1]
		sys.stdout.write(text+"\n")
	except KeyError:
		pass 
    conn.close()

if __name__ == '__main__':
        main()

