import sys

def main(filename):
	f = open(filename, 'rU')
	text=f.read().split()
	p=[]
	for ln in text:
		if ln !='0':
			print(ln,round(100*(int(ln)**.5)+(201/(int(ln)+1)+1)))
	f.close()

if __name__ == '__main__':
  main(sys.argv[1])