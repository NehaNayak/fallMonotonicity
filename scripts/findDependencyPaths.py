import sys
import pickle
from collections import defaultdict

(HEAD, REL, TAIL) = range(3)

def bfs(dep_dict,source,path):
	for dep in dep_dict[source]:
		if dep[1] == 'n1':
			return path
		elif dep[1] == 'n2':
			return path+" "+dep[2]
		else:
			

def main():
 	instances = pickle.load(sys.stdin)
    
    for instance in instances:
    	(name1,start1,end1,name2,start2,end2,rel,dep_graph,text) = instance
    	name1 = name1.replace(" ","_")
    	name1 = name2.replace(" ","_")
    	text = ["ROOT"]+text.split()
    
    	dep_dict = defaultdict(list)
    
    	for dep in dep_graph:
    		(head, rel, tail) = dep.replace("\\t","\t").split()
    		if int(head) in range(start1,end1+1):
    			head = 'n1'
    		elif int(head) in range(start2,end2+1):
    			head ='n2'
    		if int(tail) in range(start1,end1+1):
    			tail = 'n1'
    		elif int(tail) in range(start2,end2+1):
    			tail = 'n2'
    		
    		dep_dict[tail].append((rel,head,">"))
    		dep_dict[head].append((rel,tail,"<"))

	for k,v in dep_graph.iteritems():
		print k, len(v)
    
    	#paths  = bfs(dep_dict,"n1")

if __name__ == "__main__":
	main()


