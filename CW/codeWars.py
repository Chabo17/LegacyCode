import sys

def main(filename):
	f = open(filename, 'rU')
	for l in f:
		if(int(l)!=0):
			print(l[0:-1]+' gallons per week will last '+str(10000//int(l))+' weeks')
	f.close()

if __name__ == '__main__':
  main(sys.argv[1])