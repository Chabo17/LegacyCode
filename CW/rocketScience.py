import sys

def main(filename):
	f = open(filename, 'rU')
	text=f.read().split()
	for ln in text:
		print(ln)
		print(float(ln)*28.3495)
	
	
if __name__ == '__main__':
  main(sys.argv[1])