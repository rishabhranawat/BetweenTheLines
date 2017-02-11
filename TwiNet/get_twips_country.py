import tweepy
import pickle
import googlemaps
import csv
import json

gmaps = googlemaps.Client(key='AIzaSyDOVRlWChH9IbHnR1raF2sjNDvtAe24R04')

# Get countries by highest GDPs

def get_nations():
	nations = []
	with open('bin/top_100_countries.csv', 'r') as csvfile:
		spamreader = csv.reader(csvfile)
		for row in spamreader:
			nations.extend(row)
	return nations


def get_country(location):
	c = location[0]['address_components']
	for l in c:
		if("country" in l['types']):
			return l['long_name']
	return None


def get_twiplomats():
	with open("twiplomats_accounts_3.json") as f:
		d = json.load(f)
	return d

nations = get_nations()
twiplomats = get_twiplomats()

data = {}
for nation in nations: data[nation] = None

for screen_name, location in twiplomats.items():
	address = gmaps.geocode(location)
	if(address):
		country = get_country(address)
		if(country):
			data[country] = screen_name
with open("twitter_handle_with_nations", "w") as g:
	json.dump(data, g)


