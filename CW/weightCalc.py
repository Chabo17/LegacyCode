import sys

def main(filename):
	f = open(filename, 'rU')
	text=f.readlines()
	for p in text:
		ln=p.split()
		if(ln[0]!='END'):
			print("On",ln[-2],ln[0],'would weigh',(float(ln[1])*float(ln[3])),'pounds.')
	
	
if __name__ == '__main__':
  main(sys.argv[1])