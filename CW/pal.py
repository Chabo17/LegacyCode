import sys

def main(filename):
	f = open(filename, 'rU')
	text=f.read().split()
	for n in text:
		s=n
		while(s!=s[::-1]):
			num=int(s)
			d=int(s[::-1])
			t=num+d
			s=str(t)
		print(s)
		print()
	
if __name__ == '__main__':
  main(sys.argv[1])