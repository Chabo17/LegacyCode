import sys

def main(filename):
	f = open(filename, 'rU')
	text=f.read().split()
	word=''
	dict = {'A':'ab','B':'baaa','C':'baba','D':'baa','E':'a','F':'aaba','G':'bba','H':'aaaa','I':'aa','J':'abbb','K':'bab','L':'abaa','M':'bb','N':'ba','O':'bbb','P':'abba','Q':'bbab','R':'aba','S':'aaa','T':'b','U':'aab','V':'aaab','W':'abb','X':'baab','Y':'babb','Z':'bbaa'}
	for p in text:
		for l in p:
			word+=dict[l]
		if(word[::-1]==word):
			print(p+' is a MCP')
		else:
			print(p+' is *not* a MCP')
		word=''
	
if __name__ == '__main__':
  main(sys.argv[1])