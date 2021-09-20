
#problem 8
import sys
def main(filename):
	f = open(filename, 'rU')
	text=f.read().split()
	for j in range(len(text)-1):
		distinct=True
		dict={}
		for i in range(len(text[j])):
			#print(text[j][i])
			
			if text[j][i] in dict:
				
				distinct=False
				break
			else:
				dict[text[j][i]]=text[j][i]
			#print(dict[text[j][i]])
		if distinct==True:
			print(text[j] + ' USES DISTINCT LETTERS')
		else:
			print(text[j] + ' DOES NOT USE DISTINCT LETTERS')
		
	
if __name__ == '__main__':
  main(sys.argv[1])