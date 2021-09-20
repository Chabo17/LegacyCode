import requests
import sys
from bs4 import BeautifulSoup

def main():
	f= open('draft_data.csv','r')
	dudes=[]
	for ln in f:
		ln=ln[:-1]
		ln=ln.replace(',,',',#,')
		ln=ln.replace(',,',',#,')
		if ln[-1]==',':
			ln+='#'
		ln=ln.split(',')
		if ln[3][1:]=='LB':
			d=tuple(ln)
			dudes.append((d[1],[d[4],d[5],d[6],d[7],d[8],d[9],d[10],d[11],d[12],d[13]]))
	p= open('pros.csv')
	pros=[]
	for ln in p:
		ln=ln[:-1]
		ln=ln.replace(',,',',#,')
		ln=ln.replace(',,',',#,')
		if ln[-1]==',':
			ln+='#'
		ln=ln.split(',')
		d=tuple(ln)
		pros.append((d[1],[d[4],d[5],d[6],d[7],d[8],d[9],d[10],d[11],d[12],d[13]]))
	data=[]
	mean=[]
	for d in pros[2][1]:
		if d != '#':
			mean.append([float(d)])
	for d in pros:
		if d[0] != pros[2][0]:
			for da in range(0,len(d[1])):
				if d[1][da] != '#':
					mean[da].append(float(d[1][da]))
	per=[0,0,0,0,0,0,0,0,0,0]
	for i in range(0,len(per)):
		per[i]=(sum(mean[i])/len(mean[i]))
	fin =[]
	for d in dudes:
		tot=0
		p=0
		for num in range(0,len(per)):
			if d[1][num] != '#':
				p=p+(abs((float(d[1][num])-per[num])/per[num]))*100
				tot=tot+1
		fin.append((d[0],(p/tot)))
	fin = sorted(fin,key=lambda fin:fin[1])
	for p in range(0,len(fin)):
		print(str(p+1)+': '+str(fin[p][0]))


if __name__ == '__main__':
	main()