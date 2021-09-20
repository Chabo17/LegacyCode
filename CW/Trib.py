import sys

def main(filename):
	f = open(filename, 'rU')
	text=f.read().split()
	trib=[0,1,1]
	for i in range(3,31):
		trib.append(trib[i-1]+trib[i-2]+trib[i-3])
	for ln in text:
		if(int(ln)>-1):
			print(trib[int(ln)])
	
	
if __name__ == '__main__':
  main(sys.argv[1])