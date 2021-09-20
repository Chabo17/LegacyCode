import sys
import random

def main(filename):
	data=[]# the data array
	means=[]# the means array
	k=int(sys.argv[2])
	cell=[]#all of the groups
	con=1
	prev=[]#previous array
	f=open(filename).read().splitlines()

	#Replaceing all ofthe commas with spaces and putting the data in a list
	for ln in f:
		ln=ln.replace(',',' ').split()
		data.append((ln[0],float(ln[1]),float(ln[2]),float(ln[3]),float(ln[4]),float(ln[5]),float(ln[6]),float(ln[7]),float(ln[8]),float(ln[9]),float(ln[10]),float(ln[11]),float(ln[12]),float(ln[13])))

	#getting all of the means and letters in one list
	for l in data:
		means.append(((sum(l[1:])/len(l)-1),l[0]))
		
	#getting the first set of groups
	for i in range(0,k):
		ran=(random.randint(3,len(means)-3))
		cell.append((means[ran][0],[]))
	
	#having a while loop that goes through until you type quit or it 
	g=(9,10000)
	while(input()!='quit'):
		prev=cell[:]
		for n in means:
			for let in range (0,k):
				if(abs(n[0]-cell[let][0])<g[1]):
					g=(let,abs(n[0]-cell[let][0]))
			cell[g[0]][1].append(n)
			g=(9,10000)
		su=0
		temp=[]
		s=''
		
		#goes through the cells to get the new means since I can't use sum()
		for c in cell:
			for mean in c[1]:
				su+=mean[0]
			if(len(c[1])>0):
				su=(su)/(len(c[1]))
			temp.append((su,[]))
			su=0
		
		#if the current means are the same as the previous it breaks from the loop
		if(cell[0][0]==temp[0][0] and cell[1][0]==temp[1][0] and cell[2][0]==temp[2][0]): 
			break
			
		#prints out all of the letters and the means with the iteration number
		print("ITERATION "+str(con))
		for c in cell:
			print(len(c[1]),end=": ")
			for tup in c[1]:
				s+=tup[1]
			print(''.join(sorted(s)))
		con+=1
		
		#coppies the new list to cell
		cell=temp[:]
		
if __name__ == '__main__':
	main(sys.argv[1])