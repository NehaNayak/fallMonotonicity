import sys
import pickle
from collections import defaultdict

def bfs(dep_dict,source,path):
	newPaths = []
	for dep in dep_dict[source]:
		(rel, tail, dirn) = dep
		if tail in path or tail == 'n1':
			continue
		if tail=='n2':
			return " ".join([path, rel, dirn, "_END"])
		else:
			newPaths.append(bfs(\
				dep_dict,\
				tail,\
				" ".join([path, rel, dirn, tail])))
	for i in newPaths:
		if i is not None and i.endswith("_END"):
			return i

def main():
	instances = pickle.load(sys.stdin)
	
	for instance in instances:
		(name1,start1,end1,name2,start2,end2,relation,dep_graph,text) = instance
		name1 = name1.replace(" ","_")
		name2 = name2.replace(" ","_")
		text = text.split()

		dep_dict = defaultdict(list)

		for dep in dep_graph:
			(head, rel, tail) = dep.replace("\t"," ").split()
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

		path  = bfs(dep_dict,"n1","")
		try:
			if path is not None:
				path = path.split()[:-1]
				for i in range(2,len(path),3):
					path[i]=text[int(path[i])-2]
				print "\t".join([relation,":".join(path),name1,name2)
		except IndexError:
			pass
		
if __name__ == '__main__':
	main()
