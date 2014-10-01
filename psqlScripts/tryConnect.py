import psycopg2

try:
    conn = psycopg2.connect(database="kbp", user="nayakne", host="jonsson.stanford.edu", port="4242")
except:
    print "I am unable to connect to the database"

cur = conn.cursor()

cur.execute("""SELECT original_text, ner, dep_graph FROM sentence LIMIT 200000;""")

while 1:
	try:
		(text, ner, dep_graph) = cur.fetchone()
		people = [str(i) for i,tag in enumerate(ner) if tag == "PERSON"]
		places = [str(i) for i,tag in enumerate(ner) if tag == "LOCATION" or tag == "COUNTRY"]
		if len(people)>0 and len(places)>0:
			#print text 
			dep_list = [tuple(dep.replace("\\t","\t").split()) for dep in dep_graph ]
			#print ner
			#print dep_graph
			#print dep_list
		
			for dep in dep_list:
				if dep[0] in people and dep [2] in places or dep[0] in places and dep[1] in people:
					print text
					print ner
					#print dep
					#print "lalaala"
					print text[int(dep[0])],dep[1],text[int(dep[2])]
	except TypeError:
		break
conn.close()
