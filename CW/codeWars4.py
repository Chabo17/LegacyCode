import sys

def main(filename):
	f = open(filename, 'rU')
	for k in f:
		i=k.split()
		p=float(i[0])
		if(p!=0):
			q=pow(10,float(i[1]))
			h=q*p
			print("%.2f"%(float(h)))
	f.close()

if __name__ == '__main__':
  main(sys.argv[1])