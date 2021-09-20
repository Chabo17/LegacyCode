import requests
import sys
from bs4 import BeautifulSoup
from matplotlib import pyplot as plt
import re

def plot(place,text):
	dict={}
	x=[]
	y=[]
	soup = BeautifulSoup(text, 'xml')
	for state in soup.find_all('state'):
		dict[''.join(re.findall(r'<state .+ name="(.+)">',str(state)))]=re.findall(r'<point lat="(.+)" lng="(.+)"',str(state))
	if place=='all':
		for stat in dict:#graphing all of the states
			for tup in dict[stat]:
				x.append(float(tup[0]))
				y.append(float(tup[1]))
			plt.plot(y,x,color='green',marker='',linestyle='solid')
			x=[]
			y=[]
		plt.title('USA')
	else:
		for tup in dict[place]:# graphing the specific state
			x.append(float(tup[0]))
			y.append(float(tup[1]))
		y.append(float(dict[place][0][1]))
		x.append(float(dict[place][0][0]))
		plt.plot(y,x,color='green',marker='',linestyle='solid')
		plt.title(place)
	plt.xlabel("Longitude")
	plt.ylabel("Latitude")
	plt.show()
	
	
def main():
	if sys.argv[2]=='-i': # checks if you want the data off the internet or the file
		text = requests.get("http://econym.org.uk/gmap/states").text
	else:# gets data from the file
		f= open('states.xml', 'rU')
		text = f.read()
	if(len(sys.argv)>3):
		plot(''.join(sys.argv[1]+' '+sys.argv[-2]),text)
	else:
		plot(sys.argv[1],text)
	

if __name__ == '__main__':
  main()