import sys

def main(filename):
	f = open(filename, 'rU')
	text=f.read().split()
	print(text[-1])
	for ln in text:
		print(ln[-1])

		
	
	
if __name__ == '__main__':
  main(sys.argv[1])