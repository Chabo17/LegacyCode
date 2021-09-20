import sys

def wordC(filename):
	dict = {}
	f = open(filename, 'rU')
	for ln in f:
		words=ln.split()
		for word in words:
			word=word.lower()
			if (word not in dict):
				dict[word]=1
			else:
				dict[word]+=1
	f.close()
	return dict
	
def print_words(filename):
	count = wordC(filename)
	words = sorted(count.keys())
	for word in words:
		print( word, count[word])
	
def getCount(tup):
	return tup[1]

def print_top(filename):
	count = wordC(filename)
	items = sorted(count.items(), key=getCount, reverse=True)
	for item in items[:20]:
		print (item[0], item[1])
	
def main():
  if len(sys.argv) != 3:
    print( 'usage: ./wordcount.py {--count | --topcount} file')
  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    print_top(filename)
  else:
    print( 'unknown option: ' + option)

if __name__ == '__main__':
  main()