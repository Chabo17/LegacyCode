#for i in range (1,3):
#	print(i)
#print (4)
#n=[]
#for i in range (1,3):
#	n.append(i)
#print (n)
#s ="HELLO"
#for i in range (len(s),0):
#	print(s[i])
#print(s)

import sys

def main():
	Cat(sys.argv[1])
'''	
	
def Hello(s):
	print('Hello' , s,'!!!!!')

#if __name__ == '__main__':
main()
Hello(sys.argv[1])

	#dictionary stuff
	d={}
	d.keys()
	d.values()
	for k in d.keys():
		print ('key:',k,'->',d[k])
	d.items()
	for tuple in d.items():
		print (tuple)
		'''
		
	#file stuff
def Cat(filename):
	f= open(filename, 'rU')
	for line in f:
		print (line,)
	f.close()
	#split() splits on white space

if __name__ == '__main__':
	main()
