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
    
    cur.execute("""SELECT original_text, pos, ner, dep_graph FROM sentence LIMIT 200000;""")
    
    while 1:
    	try:
    		(text, pos, ner, dep_graph) = cur.fetchone()
    		people = [i for i,tag in enumerate(ner) if tag == "PERSON"]
    		places = [i for i,tag in enumerate(ner) if tag == "LOCATION" or tag == "COUNTRY"]
    		verbs = [i for i,tag in enumerate(pos) if tag in ["VB", "VBD", "VBG", "VBN", "VBP", "VBZ"]]
    		
#		print ner
#		print people
#		print places
#		print pos
		print verbs
		print text
		print dep_graph		

		if len(people)>0 and len(places)>0:

			deps_out = defaultdict(list)
    			
			for dep in dep_graph:
				(head, rel, tail) = dep.replace("\\t","\t").split()
				print head, rel, tail
				deps_out[int(head)].append((rel,int(tail)))

			for verb in verbs:
				print deps_out[verb]
				for dep1 in deps_out[verb]:
					if dep1[1] in places:
						for dep2 in deps_out[verb]:
							if dep2 in people:
								(left,right) = expandName(ner,dep1[1])
								place = "_".join(text[left:right+1])
								(left,right) = expandName(ner,dep2[1])
								person = "_".join(text[left:right+1])
								print place, "<", dep1[0], text[verb],"<", dep2[0], person
					#elif outDep[2] in people:
					#for inDep in deps_in[verb]:
				#		if outDep[2] in places and inDep[2] in people:
			#				print 
						

    		#	for dep in dep_list:
    	#			if dep[0] in people and dep [2] in places or dep[0] in places and dep[1] in people:
    #					print text
   # 					print ner
   # 					#print dep
   # 					#print "lalaala"
#					(left,right) = expandName(ner,int(dep[0]))
#					name1 = "_".join(text[left:right+1])
#					(left,right) = expandName(ner,int(dep[2]))
#					name2 = "_".join(text[left:right+1])
#    					print name1,dep[1],name2"""
    	except TypeError:
    		break
    conn.close()

if __name__ == '__main__':
        main()

