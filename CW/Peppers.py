import sys

def main(filename):
	f = open(filename, 'rU')
	text=f.read().split()
	num =[6,11,13]
	dict={6:(1,0,0),11:(0,1,0),13:(0,0,1)}
	while len(num)!=0:
		pep=num.pop(len(num)-1)
		if(pep+6<1000 and pep+6 not in dict):
			dict[pep+6]=((dict[pep][0]+1),dict[pep][1],dict[pep][2])
			num.append(pep+6)
		if(pep+11<1000 and pep+11 not in dict):
			dict[pep+11]=((dict[pep][0]),(dict[pep][1]+1),dict[pep][2])
			num.append(pep+11)
		if(pep+13<1000 and pep+13 not in dict):
			dict[pep+13]=((dict[pep][0]),dict[pep][1],(dict[pep][2]+1))
			num.append(pep+13)
	tup=(dict.get(int(text[0])))
	if tup != None:
		print(text[0],"peppers can be packed most economically in:")
		if tup[2]==1:
			print('1 package of 13')
		else:
			print(tup[2],'packages of 13')
		if tup[1]==1:
			print('1 package of 11')
		else:
			print(tup[1],'packages of 11')
		if tup[0]==1:
			print('1 package of 6')
		else:
			print(tup[0],'packages of 6')
		print(sum(tup),'total packages')
	else:
		print(text[0],'peppers cannot be packed')
		
if __name__ == '__main__':
  main(sys.argv[1])