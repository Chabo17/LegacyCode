import sys
from collections import Counter
from matplotlib import pyplot as plt

def Prob7(text):
	pval=[]
	rval=[]
	for ln in text:
		if float(ln) != 0:#finds the p val and r val
			p=float(ln)
			pval.append(p)
			rval.append(p**(2/3))
	plt.plot(pval,rval,marker='o',color='blue',linestyle='')#plots all of the dots
	for i in range (0,35):
		plt.plot([i,i+1],[i**(2/3),(i+1)**(2/3)])#plots the line
	plt.title("Kepler's Third Law")#title
	plt.ylabel("R values")#y axis title
	plt.xlabel("P values")#x axis
	plt.show()
	
	
def Prob8(text):
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
	x=["Empty Cubes","Duplicate Cubes","Employees without Cube"]#names of the bars
	y=[e,dup,dict['0']]#value of the barss
	xs = [i+.1  for i, _ in enumerate(x)]
	plt.xticks([i + .5 for i, _ in enumerate(x)],x)
	plt.xlabel("Number of cubes")
	plt.bar(xs,y)
	plt.title("Problem 8")
	plt.show()
	
def Prob9(text):
	c=Counter()
	for i in range (0,len(text)-1,2):#makes the counter and adds the values
		c[text[i]]+=int(text[i+1])
	print(c.most_common(5))
	
	

	
		
def main(filename):
	f = open(filename, 'rU')
	text=f.read().split()
	if sys.argv[2]=='-prob7':
		Prob7(text)
	elif sys.argv[2]=='-prob8':
		Prob8(text)
	else:
		Prob9(text)
		
if __name__ == '__main__':
  main(sys.argv[1])
  