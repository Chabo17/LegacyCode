import sys
from matplotlib import pyplot as plt
import collections
import statistics

def main(filename):
	f=open(filename).read().replace(',',' ').splitlines()
	dict={}
	f=f[1:]
	for ln in f:
		ln=ln.split()
		if len(ln)==6:
			ln=[ln[0],((ln[1])+' '+ln[2]),ln[3],ln[4],ln[5]]
		if len(ln)==7:
			ln=[ln[0],(ln[1]+' '+ln[2]+' '+ln[3]),ln[4],ln[5],ln[6]]
		if ln[1].title() not in dict:
			dict[ln[1].title()]=[int(ln[-2])]
		else:
			dict[ln[1].title()].append(int(ln[-2]))
	
	tup=dict.items()
	q=[]
	f=[]
	for d in tup:
		q.append((d[0],(d[1])))
	q=sorted(q,key=lambda q:len(q[1]))
	for i in range(0,100):
		f.append((q[i][0],statistics.median(q[i][1])))
	t=sorted(f,key=lambda f:-f[1])
	for i in range(0,100):
		print('{:<20}'.format(t[i][0]),end='')
		print('{:<20}'.format(t[i][1]))

def num(t):
	return t[1][1]
		
if __name__ == '__main__':
	main('tree.csv')