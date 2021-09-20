import sys

def main(filename):
	f = open(filename, 'rU')
	text=f.read().split()
	win =[]
	for i in range (2,len(text)-1,2):
		if ( abs(int(text[i])-int(text[0]))< abs(win[0]-int(text[0]))):
			
	print()
		
	f.close()

if __name__ == '__main__':
  main(sys.argv[1])