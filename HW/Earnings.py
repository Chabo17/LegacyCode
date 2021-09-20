import io
import json
import sys
import requests
from matplotlib import pyplot as plt

def main():
	
	with io.open('gov.json') as cred:
		creds=json.load(cred)
		key=creds['api_key']
		# median_debt.completers.overall
		# median_debt.noncompleters
		# median_debt.dependent_students
		# median_debt.independent_students
		base_url = 'https://api.data.gov/ed/collegescorecard/v1/schools?fields=school.name,id,2014.aid.median_debt.completers.overall,2014.aid.median_debt.noncompleters&page=1&_per_page=100'
		school = "California"
		key_param= "&api_key="+key
		
		dif=[]
		
		full_query = base_url +school+key_param
		
		data = requests.get(full_query)
		
		text=str(data.json)
		txt = open('edata.json', 'w')
		text=text.encode("ascii","ignore")
		txt.write(str(data.text))
	
	with open('edata.json','r') as f:
		data = json.loads(f.read())
		name=[]
		comp=[]
		incomp=[]
		
		for i in data['results']:
			if(i["2014.aid.median_debt.noncompleters"] is not None and i["2014.aid.median_debt.completers.overall"] is not None):
				dif.append((i["school.name"],(int(i["2014.aid.median_debt.completers.overall"])-int(i["2014.aid.median_debt.noncompleters"]))))
				name.append(i["school.name"])
				comp.append(int(i["2014.aid.median_debt.completers.overall"]))
				incomp.append(int(i["2014.aid.median_debt.noncompleters"]))
				
				
		data=list(zip(name,comp,incomp))
		data=sorted(data)

		width=1
		xs = [i for i, _ in enumerate(comp)]
		xy = [i for i, _ in enumerate(incomp)]
		plt.bar(xs,comp,width,label='Completed College',color='b')
		plt.bar(xy,incomp,width,color='r',label="Didn't Complete College")
		plt.ylabel('Money in USD')
		plt.xticks([i+10 for i, _ in enumerate(comp)],'')
		plt.title("Median Debt After College")
		plt.xlabel("Schools")
		plt.legend(loc=1)
		dif=sorted(dif,key=tup)
		for i in range (0,len(dif)):
			print("{:<60}".format(dif[i][0]),end="")
			print("{:<25}".format(dif[i][1]))
		plt.show()
def tup(tuple):
	return tuple[-1]
		
if __name__ == '__main__':
	main()