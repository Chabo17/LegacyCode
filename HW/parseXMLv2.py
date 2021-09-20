import sys
import re
from bs4 import BeautifulSoup

def extract(filename):
	
	f = open(filename, 'rU')
	text = f.read()
	soup = BeautifulSoup(text, 'xml')
	auth=[]
	title=[]
	pr=[]
	for aut in soup.find_all('author'):
		auth.append(aut.get_text())
	for t in soup.find_all('title'):
		title.append(t.get_text())
	for p in soup.find_all('price'):
		pr.append(float(p.get_text()))
	tup=list(zip(auth,title,pr))
	return tup
	
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
	for triple in tuple:
		print("{:<25}".format(triple[0]),end="")
		print("{:<50}".format(triple[1]),end="")
		print("{:<25}".format(triple[2]))
	
if __name__ == '__main__':
  main()