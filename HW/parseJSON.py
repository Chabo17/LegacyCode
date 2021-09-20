import sys
import re
import json

def main():
	with open(sys.argv[1],'r') as f:
		data = json.loads(f.read())
		titles= []
		rat=[]
		url=[]
		for i in range (0,10):
			titles.append(data['query']['results']['Result'][i]['Title'])
			url.append(data['query']['results']['Result'][i]['Url'])
			rat.append(data['query']['results']['Result'][i]["Rating"]["AverageRating"])
		data=list(zip(titles,rat,url))
		data=sorted(data)
		for triple in data:
			print("{:<50}".format(triple[0]),end="")
			print("{:<25}".format(triple[1]),end="")
			print("{:<25}".format(triple[2]))

if __name__ == '__main__':
  main()