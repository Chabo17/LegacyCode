import sys

def main(filename):
	f = open(filename, 'rU')
	text=f.read().split()
	c=0

	l=''
	dict = ["DON'T", "CAN'T", "ISN'T", "HAVEN'T", "CANNOT", "WOULDN'T", "COULDN'T", "WON'T", "NO","NOT", "NEVER","NOBODY","NOWHERE","NEITHER","AIN'T"]
	for ln in text:
		if(len(ln)>3):
			ln=ln.replace('"','')
			ln=ln.replace(',','')
			l+=ln+' '
			if(ln in dict):
				c+=1
			if('.' in ln):
				if(ln[:-1] in dict):
					c+=1
			if(ln[-1]=='.'or ln[-1]=='!'):
				print(c,l)
				c=0
				l=''
	print()
	

if __name__ == '__main__':
  main(sys.argv[1])