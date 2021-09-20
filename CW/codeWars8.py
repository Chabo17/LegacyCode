import sys

def main(filename):
	f = open(filename, 'rU')
	text=f.read().split()
	dup=0
	e=0
	dict={}
	for i in range (2,len(text),2):
		if text[i-1]=='NA':
			e+=1
		else:
			if(text[i] not in dict):
				dict[text[i]]=1
			else:
				dict[text[i]]+=1
	for d in dict:
		if(dict[d]>1 and d!='0'):
			dup+=1
	print("Empty Cubes:",e)
	print("Duplicate Cube Assignments:",dup)
	print("Employees without Cube",dict['0'])
			
if __name__ == '__main__':
  main(sys.argv[1])
  