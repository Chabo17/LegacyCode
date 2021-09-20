import sys

def main(filename):
	f = open(filename, 'rU')
	text=f.read().split()
	for ln in text:
		if float(ln) != 0:
			p=float(ln)
			r=p**2
			R=r**(1/3)
			print(R)

	
	
if __name__ == '__main__':
  main(sys.argv[1])
  