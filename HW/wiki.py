import requests
import sys
import io
import json
from bs4 import BeautifulSoup
import re
import wikipedia

def main():
	'''
	with io.open('wiki.json') as cred:
		creds=json.load(cred)
		key=creds['api_key']
	'''
	
	base_url='https://en.wikipedia.org/w/api.php'
	key_param= "&api_key="+key
	full_query = base_url +school+key_param
	data = requests.get(full_query)
	

if __name__ == '__main__':
  main()