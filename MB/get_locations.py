import json
from geopy.geocoders import Nominatim


import tweepy
import json
import pprint
import googlemaps


def get_state(location):
	c = location[0]['address_components']
	for l in c:
		if("administrative_area_level_1" in l['types']):
			return l['long_name']

	return None

with open("resist_1000.json") as f:
	bs = json.load(f)

gmaps = googlemaps.Client(key='AIzaSyAID1o6hSjBt4ucm-f1WLXyAeV5vK0SNPk')

bsr = {}
count = 0

with open("resist.json", "w") as fp:
	for tweet, address in bs.items():
		count += 1
		location = gmaps.geocode(address)
		if(location):
			state = get_state(location)
			print(count, state)
			if(state):
				try:
					bsr[state] += 1
				except:
					bsr[state] = 1
	json.dump(bsr, fp)
