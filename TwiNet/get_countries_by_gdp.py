from bs4 import BeautifulSoup
import urllib
from urllib.request import Request, urlopen
import csv
import json
import pprint

wiki = "http://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)"
header = {'User-Agent': 'Mozilla/5.0'} #Needed to prevent 403 error on Wikipedia
req = Request(wiki,headers=header)
page = urlopen(req)
soup = BeautifulSoup(page)
table = soup.find("table", { "class" : "wikitable sortable" })

all_countries = []
countries = 0
for row in table.findAll("tr"):
	if(countries >= 100):
		break
	cells = row.findAll("td")
	if(len(cells) > 1):
		country = cells[1].text
		if("World" not in country and "European Union" not in country):
			countries += 1
			all_countries.append(country.split("[")[0].lstrip())

heads = {}


wiki = "http://en.wikipedia.org/wiki/List_of_current_heads_of_state_and_government"
header = {'User-Agent': 'Mozilla/5.0'} #Needed to prevent 403 error on Wikipedia
req = Request(wiki,headers=header)
page = urlopen(req)
soup = BeautifulSoup(page)
table = soup.find("table", { "class" : "wikitable plainrowheaders" })

for row in table.findAll("tr"):
	leader = None
	cells = row.findAll("td")
	states = row.findAll("th")

	if(len(states) > 0):
		state = states[0].text.split("[")[0].lstrip()
		if(state in all_countries):
			if(len(cells) == 0):
				print(state)
			if(len(cells) == 2):
				leader = cells[1].text.split("[")[0]
			elif(len(cells) == 1):
				leader = cells[0].text.split("[")[0]
			if(leader):
				heads[state] = leader.replace("\xa0", "").lstrip()

heads["United States"] = "President – Donald Trump"
heads["Switzerland"] = "President - Doris Leuthard"

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(heads)


with open("heads_of_states_94.json", "w") as f:
	json.dump(heads, f)
