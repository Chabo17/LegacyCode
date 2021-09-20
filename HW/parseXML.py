import sys
import re

def extract(filename):	
	f = open(filename, 'rU')
	text = f.read()
	data=[]#holds the data
	tuples = (re.findall(r'<author>(.+)</author>', text),re.findall(r'<title>(.+)</title>', text),re.findall(r'<price>(.+)<', text))
	for i in range(len(tuples[0])):# this for loop turns the tupple of arrays into an array of tuples
		data.append(((tuples[0][i]),(tuples[1][i]),float(tuples[2][i])))
	return data
	
def auth(tuple):#the key for sorting the authors and it returns the author
	return tuple[0]
	
def pr(tuple):#the key for sorting the price and it returns the price
	return tuple[2]

def main():
	args = sys.argv[2]#finds out how you want to sort tuple
	tuple=extract(sys.argv[1])
	if args == '--author':#sorts alphabeticaly with author
		tuple=sorted(tuple,key=auth)
	elif args == '--price':#sorts with the heighest price first
		tuple=sorted(tuple,key=pr,reverse=True)
	print(tuple)
	
if __name__ == '__main__':
  main()