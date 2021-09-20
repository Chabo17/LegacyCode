import sys

def main(filename):
	f = open(filename, 'rU')
	text=f.read().split()
	dict={}
	for i in range(0,len(text)-1,2):
		if text[i] not in dict:
			dict[text[i]]=int(text[i+1])
		else:
			dict[text[i]]+=int(text[i+1])
	for i in range(1,6):
		max='0'
		for d in dict:
			if int(dict[d])>int(dict[max]):
				max=d
		print(i,max,dict[max])
		dict[max]='0'
		
	
	
if __name__ == '__main__':
  main(sys.argv[1])
  