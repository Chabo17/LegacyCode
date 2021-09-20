import sys

def main(filename):
	f = open(filename, 'rU')
	text=f.read().split()
	for ln in text:
		print((int(ln)*8)-95)
	
	
if __name__ == '__main__':
  main(sys.argv[1])