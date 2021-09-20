import sys

def main(filename):
	f = open(filename, 'rU')
	text=f.read().split()
	for ln in text:
		if(int(ln)>-1):
			if(int(ln)<10):
				print(str(int(12-int(ln)/5))+':'+ln+'0')
			else:
				print(str(int(12-int(ln)/5))+':'+ln)	
	
if __name__ == '__main__':
  main(sys.argv[1])