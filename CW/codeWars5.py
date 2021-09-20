import sys

def main(filename):
	s=''
	f = open(filename, 'rU')
	q=f.read().split()
	q=q[1:]
	for i in range(0,len(q)-1,2):
		tuple=(int(q[i]),q[i+1])
		for k in range(0,len(tuple[1])):
			if k % tuple[0]!=0:
				print(tuple[1][k],end='')
		print(s)

if __name__ == '__main__':
  main(sys.argv[1])