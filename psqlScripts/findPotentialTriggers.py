import psycopg2
from collections import defaultdict

def expandName(ner, index):

	leftMost = rightMost = index
	
	while(True):
		if leftMost>0 and ner[leftMost-1]==ner[index]:
			leftMost-=1
		else:
			break
	
	while(True):
		if rightMost<(len(ner)-1) and ner[rightMost+1]==ner[index]:
			rightMost+=1
		else:
			break

	return(leftMost,rightMost)

def main():    

    try:
        conn = psycopg2.connect(database="kbp", user="nayakne", host="jonsson.stanford.edu", port="4242")

    except:
        print "I am unable to connect to the database"
    
    cur = conn.cursor()
    
    cur.execute("""SELECT original_text, pos, ner, dep_graph, sentence_id FROM sentence;""")
    
    while 1:
    	try:
    		(text, pos, ner, dep_graph, id) = cur.fetchone()

		depText = ["ROOT"]+text

    		people = [i for i,tag in enumerate(ner) if tag == "PERSON"]
    		places = [i for i,tag in enumerate(ner) if tag == "LOCATION" or tag == "COUNTRY"]

    		verbs = [i for i,tag in enumerate(pos) if tag in ["VB", "VBD", "VBG", "VBN", "VBP", "VBZ"]]
    		
		if len(people)>0 and len(places)>0:

			deps_out = defaultdict(list)
    			
			for dep in dep_graph:
				(head, rel, tail) = dep.replace("\\t","\t").split()
				#print head, rel, tail
				deps_out[int(tail)-1].append((rel,int(head)-1))
				deps_out[int(head)-1].append((rel,int(tail)-1))

			output = set()
			for verb in verbs:
				#print deps_out[verb]
				for dep1 in deps_out[verb]:
					if dep1[1] in places:
						for dep2 in deps_out[verb]:
							if dep2[1] in people:
				#				print "==="
				#				print text
				#				print dep_graph
				#				print ner
								(left,right) = expandName(ner,dep1[1])
								place = "_".join(text[left:right+1])
								(left,right) = expandName(ner,dep2[1])
								person = "_".join(text[left:right+1])
								output.add(place+"\t"+dep1[0]+"\t"+text[verb]+"\t"+dep2[0]+"\t"+person+"\t"+id)
			if len(output)>0:
				for i in output:
					print i
    	except TypeError:
    		break
    conn.close()

if __name__ == '__main__':
        main()

