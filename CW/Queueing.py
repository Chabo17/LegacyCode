import sys

def main(filename):
	f = open(filename, 'rU')
	text=f.read().splitlines()
	fin=''
	dict={'Q1':[],'Q2':[],'Q3':[],'Q4':[],'Q5':[],'Q6':[],'Q7':[],'Q8':[],'Q9':[]}
	for i in range(0,int(text[0][:2])):
		fin+=' '
	for j in range(1,int(text[0][-2:])+1):
		ln=text[j].split()
		dict[ln[0]].append((int(ln[1]),ln[2]))
	for q in text[-1].split():
		temp = dict[q].pop(0)
		fin =fin[:temp[0]]+temp[1]+fin[temp[0]+len(temp[1]):]
	print(fin)

if __name__ == '__main__':
  main(sys.argv[1])