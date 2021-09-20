import sys
from matplotlib import pyplot as plt
import collections

def main():
	f = open("iris.data.training")#oppening the training data
	text=f.read()
	text=text.replace(',',' ')#replacing all of the commas with spaces so it will split correctly
	text =text.splitlines()
	data=[]
	test=open('iris.data.testing')#oppening test data
	test=test.read()
	test=test.replace(',',' ')# preparing it to split
	test=test.splitlines()
	testdata=[]
	cor=(0,0,0,0)
	vir =False
	set=False
	for ln in text:#appending all of the trainig into a list for plotting latter
		lin=ln.split()
		data.append((float(lin[0]),float(lin[1]),float(lin[2]),float(lin[3]),lin[-1]))
	for t in test:# getting all of the test data
		lin=t.split()
		testdata.append((float(lin[0]),float(lin[1]),float(lin[2]),float(lin[3]),lin[-1]))
	if sys.argv[-1]=='-2':
		for tup in data:
			for i in range (221,225):#graphing all of the training data into subplots
				plt.subplot(i)
				if tup[-1]=='Iris-virginica':
					plt.plot(tup[2],tup[3],marker='.',color='g')
				elif tup[-1]=='Iris-setosa':
					plt.plot(tup[2],tup[3],marker='.',color='b')
				else:
					plt.plot(tup[2],tup[3],marker='.',color='r')
	for i in testdata:
		dist=[]
		if sys.argv[-1]=='-2':#making all the distances depending on what n you want (4 is default)
			for k in data:
				dist.append(((((i[2]-k[2])**2)+((i[3]-k[3])**2)),k[-1]))
		else:
			for k in data:
				dist.append(((((i[0]-k[0])**2)+((i[1]-k[1])**2)+(((i[2]-k[2])**2)+((i[3]-k[3])**2)),k[-1])))
		dist=sorted(dist) #sorting everything 
		type=(0,0,0)
		fin=[]
		for q in range(0,10):#this loop is going to go through each of the k's
			if dist[q][-1]=='Iris-virginica':#keeping track of the recent types
				type=(type[0]+1,type[1],type[2])
			elif dist[q][-1]=='Iris-versicolor':
				type=(type[0],type[1]+1,type[2])
			else:
				type=(type[0],type[1],type[2]+1)
			if q==0 or q==2 or q==4 or q==9:
				if type[0]>=type[1] and type[0]>=type[2]:
					fin.append('Iris-virginica')
				elif type[1]>=type[0] and type[1]>=type[2]:
					fin.append('Iris-versicolor')
				else:
					fin.append('Iris-setosa')
				cnt=collections.Counter(fin)
				what=list(cnt)
				if what[0]==i[-1]:# comparing the test with what the closest n flowers
					if sys.argv[-1]=='-2' and q==0:#k=0
						cor=(cor[0]+1,cor[1],cor[2],cor[3])
						plt.subplot(221)
						plt.title('k=1')
						if i[-1]=='Iris-virginica':
							plt.plot(i[2],i[3],marker='^',color='g')
						elif i[-1]=='Iris-versicolor':
							plt.plot(i[2],i[3],marker='^',color='r')
						else:
							plt.plot(i[2],i[3],marker='^',color='b')
					elif sys.argv[-1]=='-2' and q==2:#k=3
						cor=(cor[0],cor[1]+1,cor[2],cor[3])
						plt.subplot(222)
						plt.title('k=3')
						if i[-1]=='Iris-virginica':
							plt.plot(i[2],i[3],marker='^',color='g')
						elif i[-1]=='Iris-versicolor':
							plt.plot(i[2],i[3],marker='^',color='r')
						else:
							plt.plot(i[2],i[3],marker='^',color='b')
					elif sys.argv[-1]=='-2' and q==4:#k=5
						cor=(cor[0],cor[1],cor[2]+1,cor[3])
						plt.subplot(223)
						plt.title('k=5')
						if i[-1]=='Iris-virginica':
							plt.plot(i[2],i[3],marker='^',color='g')
						elif i[-1]=='Iris-versicolor':
							plt.plot(i[2],i[3],marker='^',color='r')
						else:
							plt.plot(i[2],i[3],marker='^',color='b')
					elif sys.argv[-1]=='-2' and q==9:#k=10
						cor=(cor[0],cor[1],cor[2],cor[3]+1)
						plt.subplot(224)
						plt.title('k=10')
						if i[-1]=='Iris-virginica':
							plt.plot(i[2],i[3],marker='^',color='g')
						elif i[-1]=='Iris-versicolor':
							plt.plot(i[2],i[3],marker='^',color='r')
						else:
							plt.plot(i[2],i[3],marker='^',color='b')
				else:#Now we do the same process if it is wrong (for extra data sets)
					if sys.argv[-1]=='-2' and q==0:
						plt.subplot(221)
						plt.title('k=1')
						if what[0]=='Iris-virginica':
							plt.plot(i[2],i[3],marker='x',color='g')
						elif what[0]=='Iris-versicolor':
							plt.plot(i[2],i[3],marker='x',color='r')
						else:
							plt.plot(i[2],i[3],marker='x',color='b')
					elif sys.argv[-1]=='-2' and q==2:
						plt.subplot(222)
						plt.title('k=3')
						if what[0]=='Iris-virginica':
							plt.plot(i[2],i[3],marker='x',color='g')
						elif what[0]=='Iris-versicolor':
							plt.plot(i[2],i[3],marker='x',color='r')
						else:
							plt.plot(i[2],i[3],marker='x',color='b')
					elif sys.argv[-1]=='-2' and q==4:
						plt.subplot(223)
						plt.title('k=5')
						if what[0]=='Iris-virginica':
							plt.plot(i[2],i[3],marker='x',color='g')
						elif what[0]=='Iris-versicolor':
							plt.plot(i[2],i[3],marker='x',color='r')
						else:
							plt.plot(i[2],i[3],marker='x',color='b')
					elif sys.argv[-1]=='-2' and q==9:
						plt.subplot(224)
						plt.x
						plt.title('k=10')
						if what[0]=='Iris-virginica':
							plt.plot(i[2],i[3],marker='x',color='g')
						elif what[0]=='Iris-versicolor':
							plt.plot(i[2],i[3],marker='x',color='r')
						else:
							plt.plot(i[2],i[3],marker='x',color='b')
	print('For k =1 there was a %'+str((cor[0]/len(testdata))),'sucess rate')#printing out all of te sucess rates for all of the ks
	print('For k =3 there was a %'+str((cor[1]/len(testdata))),'sucess rate')
	print('For k =5 there was a %'+str((cor[2]/len(testdata))),'sucess rate')
	print('For k =10 there was a %'+str((cor[3]/len(testdata))),'sucess rate')
	
	if sys.argv[-1]=='-2':
		plt.show()
		
if __name__ == '__main__':
	main()