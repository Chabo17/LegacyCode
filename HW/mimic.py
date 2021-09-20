import random
import sys

def mimic_dict(filename):
	dict = {}
	f = open(filename, 'rU')
	text = f.read()
	words = text.split()
	prev = ''
	for word in words:
		if not prev in dict:
			dict[prev] = [word]
		else:
			dict[prev].append(word)
		prev = word
	f.close()
	return dict

def print_mimic(mimic_dict, word):
	a=''
	for i in range (0,300):
		word =random.choice(mimic_dict[word])
		a=a +' '+word
	print(a)

def main():
	if len(sys.argv) != 2:
		print ('usage: ./mimic.py file-to-read')		
	dict = mimic_dict(sys.argv[1])
	print_mimic(dict, '')


if __name__ == '__main__':
  main()