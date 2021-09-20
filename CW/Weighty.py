import sys

def main(filename):
	f = open(filename, 'rU')
	text=f.readlines()
	we=[]
	for p in text:
		ln=p.split()
		pair=[]
		for i in ln:
			pair.append(int(i))
		pair=sorted(pair)
		we.append(int((sum(pair)/4)-(pair[0]+pair[9])))
		we.append(pair[1]-we[0])
		we.append(pair[0]-we[1])
		we.append(pair[8]-we[0])
		we.append(pair[9]-we[3])
		we=sorted(we)
		for s in we:
			print(s,end=' ')
		print()
		we=[]
				
	
if __name__ == '__main__':
  main(sys.argv[1])