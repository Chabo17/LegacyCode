import sys

def main(filename):
	f = open(filename, 'rU')
	text=f.read().splitlines()
	for ln in text[1:]:
		num=[]
		ln=ln.split()
		for i in ln:
			num.append(int(ln[0]))
			a=int(ln[1])
			b=int(ln[2])
			c=int(ln[3])
			m=int(ln[4])
			n=int(ln[5])
			e=float(ln[-1])
			num.append(c+(a*num[0]+m)/(b*num[0]+n))
			con=0
			while(abs(num[-1]-num[-2])>=e):
				num.append((c+(a*num[-1]+m)/(b*num[-1]+n)))
				con+=1
				if con==100:
					break
		print(num[-1])

if __name__ == '__main__':
  main(sys.argv[1])