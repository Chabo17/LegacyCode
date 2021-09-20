import sys

def main(filename):
	f = open(filename, 'rU')
	text=f.read()
	mil=0
	for ln in text:
		if(len(ln)>3):
			if(num=='1'):
				mil+=2
			elif(num=='7'):
				mil+=3
			elif(num=='4'):
				mil+=4
			elif(num=='2'or num=='3' or num=='5'):
				mil+=5
			elif(num=='6' or num=='9' or num=='0'):
				mil+=6
			elif(num=='8'):
				mil+=7
		mil=((mil*15)+20)
		print(mil, 'milliamps')
		mil=0
	f.close()

if __name__ == '__main__':
  main(sys.argv[1])