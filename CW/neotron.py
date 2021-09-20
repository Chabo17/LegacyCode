import sys

def main(filename):
	f = open(filename, 'rU')
	text=f.read().split()
	s=text[0]
	s=''.join(sorted(s))
	file=text[1:]
	temp=''
	fin =[]
	b=True
	for i in file:
		for k in file:
			for j in file:
				w=i+k+j
				w=''.join(sorted(w))
				if(w==s):
					fin.append(i)
					fin.append(k)
					fin.append(j)
					fin=(sorted(fin))
					print(fin[0],fin[1],fin[2])
					sys.exit()
			

	
if __name__ == '__main__':
  main(sys.argv[1])