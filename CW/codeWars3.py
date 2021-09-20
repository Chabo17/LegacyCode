import sys

def main(filename):
	f = open(filename, 'rU')
	q=f.read()
	k=q.split()
	
	for w in k:
		l=False
		if(len(w)>2):
			for i in range (0,len(w)-1):
				if(w[i]==w[i+1]):
					print('likes',w)
					l=True
			if(l==False):
				print('hates',	w)
	f.close()

if __name__ == '__main__':
  main(sys.argv[1])