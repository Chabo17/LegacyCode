import sys
import re
import glob

def extract_names(filename):
	names = []
	g = []
	b = []
	
	f = open(filename, 'rU')
	text = f.read()
  
	years = re.search(r'Popularity\sin\s(\d\d\d\d)', text)#finds the year
	year = years.group(1)
	print(year)
	tuples = re.findall(r'<td>(\d+)</td><td>(\w+)</td>\<td>(\w+)</td>', text)#goes throught the html file finding the names
	ranks =  {}
	for tuple in tuples:#looks in the tuple to find each of the names
		(rank, boy, girl) = tuple  
		if boy not in ranks:# singles out the boys names
			ranks[boy] = rank
		if girl not in ranks:#singles out the girls names
			ranks[girl] = rank
	for name in ranks:#adds all the names to the list
		names.append(name + " " + ranks[name])
	names=sorted(names)
	return names


def main():
	args = sys.argv[1:]
	summary=False
	if '*' in sys.argv[-1:]:
		sys.argv[-1:] = glob.glob(sys.argv[-1])
	if args[0] == '--summaryfile':
		summary = True	
	for filename in glob.glob(sys.argv[-1]):
		names = extract_names(filename)
		text = '\n'.join(names)
	if summary:
		txt = open(filename + '.summary', 'w')
		txt.write(text)
		txt.close()
	else:
		print (text)

if __name__ == '__main__':
  main()