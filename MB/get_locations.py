import json
from geopy.geocoders import Nominatim
import googlemaps

import tweepy
import json
import pprint

def get_state(location):
	c = location[0]['address_components']
	for l in c:
		if("administrative_area_level_1" in l['types']):
			return l['long_name']

	return None

with open("delete_uber_max.json") as f:
	bs = json.load(f)


with open("finalData/stateab.json") as f:
	ab = json.load(f)

all_states = []
for each in ab:
	all_states.append(each["name"])

gmaps = googlemaps.Client(key='AIzaSyDOVRlWChH9IbHnR1raF2sjNDvtAe24R04')

bsr = {}
count = 0
total = 1

with open("uber.json", "w") as fp:
	for tweet, address in bs.items():
		if(total==638):
			break
		location = gmaps.geocode(address)
		if(location):
			state = get_state(location)
			print(total, state)
			if(state and state in all_states):
				try:
					total += 1
					bsr[state] += 1
				except:
					bsr[state] = 1
	json.dump(bsr, fp)
