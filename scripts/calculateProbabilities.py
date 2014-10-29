import sys
from collections import defaultdict

def defaultdicthelper():
	return defaultdict(int)

def main():
	joint = open(sys.argv[1],'r')
	joint_dict = defaultdict(defaultdicthelper)

	relation_prior = open(sys.argv[2],'r')
	relation_prior_dict = defaultdict(int)

	path_prior = open(sys.argv[3],'r')
	path_prior_dict = defaultdict(int)

	for line in joint:
		(relation, path, freq) = line.split("\t")
		joint_dict[relation][path]=int(freq)
	for line in relation_prior:
		(relation, freq) = line.split("\t")
		relation_prior_dict[relation]=int(freq)
	for line in path_prior:
		(path, freq) = line.split("\t")
		path_prior_dict[path]=int(freq)

	for relation, paths in joint.iteritems():
		for path, freq in paths.iteritems():
			values = [relation, path, float(freq)/float(relation_prior_dict[relation],float(freq)/float(path_prior_dict[relation])]
			sys.stdout.write("\t".join(values)+"\n")

if __name__ == '__main__':
	main()