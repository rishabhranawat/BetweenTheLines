from bs4 import BeautifulSoup
import urllib
from urllib.request import Request, urlopen
import csv

wiki = "http://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)"
header = {'User-Agent': 'Mozilla/5.0'} #Needed to prevent 403 error on Wikipedia
req = Request(wiki,headers=header)
page = urlopen(req)
soup = BeautifulSoup(page)

table = soup.find("table", { "class" : "wikitable sortable" })

with open("top_100_countries.csv", "w") as f:
	writer = csv.writer(f)
	countries = 0
	for row in table.findAll("tr"):
		if(countries >= 100):
			f.close()
			break
		cells = row.findAll("td")
		if(len(cells) > 1):
			country = cells[1].text
			if("World" not in country and "European Union" not in country):
				countries += 1
				print(country)
				writer.writerow([country.split("[")[0].lstrip()])
