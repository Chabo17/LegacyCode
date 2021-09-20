import sys

def main(filename):
	f = open(filename, 'rU')
	text=f.read().splitlines()
	
	for ln in text:
		even=0
		l=ln.split()
		for i in range (int(l[0]),int(l[1])+1):
			if bin(i).count('1')%2==0:
				even+=1
		print(even)
		
	

if __name__ == '__main__':
  main(sys.argv[1])