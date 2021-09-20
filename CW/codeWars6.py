import sys

def main(filename):
	f = open(filename, 'rU')
	text=f.read().split()
	data=1
	for ln in text:
		data=data*int(ln)
	data=data/27
	print(int(round(data)))
	
	
if __name__ == '__main__':
  main(sys.argv[1])
  