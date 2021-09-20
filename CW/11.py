import sys

def main(filename):
	f = open(filename, 'rU')
	text=f.read().split()
	n = text[0]
	print(text[0])
	while(len(str(n))>2):
		s=n[-1]
		n=n[:-1]
		n=int(n)
		s=int(s)
		n=n-s
		n=str(n)
		print(n)
	print()
	if(int(n)%11==0):
		print('The number ',text[0],'is divisible by 11')
	else:
		print('The number'+text[0],'is not divisible by 11')
	
	
if __name__ == '__main__':
  main(sys.argv[1])