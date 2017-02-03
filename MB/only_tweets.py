import tweepy
import json
import pprint
import time
import pickle

import googlemaps

auth = tweepy.OAuthHandler("zIapCtcYvVdzCMaocAuCc3L4Y",
	"PgBlMAU5JSsd7cQyYFlHgwjtQesFmRH5KbSZLPIw5861WRGNoT")
auth.set_access_token("826903475262980098-PSEGqBRhHUhQ95ZfrigieWZoyTwDRDG", 
	"dkN4Da7RhecnOvMWd4cxQwFaSSeLFvTWsvlUPHCYJ8HQ6")
api = tweepy.API(auth)

gmaps = googlemaps.Client(key='AIzaSyCNlfqMEJEdG97-tDde8hfOUxy02z149xA')

# Getting the first batch
batch = api.search("#FakeTears", count=100)
oldest = batch[-1].id-1

with open("finalData/stateab.json") as f:
	ab = json.load(f)

all_states = []
for each in ab:
	all_states.append(each["name"])

def get_state(location):
	c = location[0]['address_components']
	for l in c:
		if("administrative_area_level_1" in l['types']):
			return l['long_name']

	return None

tweets = []
data = {}
total = 0
collect = True
# Open the json file and keep adding the tweets
with open("fake_tears.json", "w") as f:
	while(collect and len(batch) > 0):
		if(not collect): break
		for tweet in batch:
			if(total >= 700):
				print("here!")
				collect = False
				break
			tweets.append(tweet)
			address = tweet.user.location
			location = gmaps.geocode(address)
			if(location):
				state = get_state(location)
				if(state and state in all_states):
					try:
						total += 1
						data[state] += 1
					except:
						total += 1
						data[state] = 1

		batch = api.search("#FakeTears", count=100, max_id=oldest)
		oldest = batch[-1].id-1
	json.dump(tweets, f)

with open("fake_tears_data", "wb") as f:
	pickle.dump(tweets, f)
