import tweepy
import json
import pprint
import time


def get_state(location):
	c = location[0]['address_components']
	for l in c:
		if("administrative_area_level_1" in l['types']):
			return l['long_name']

	return None

# Twitter authorization
auth = tweepy.OAuthHandler("7ORmqhp1lXxpazSzpTGVVNAv6", 
	"KXwjMsUcf0cKLIZ94D76GYwJeAhQ2qbUlxp2OnENVDQXIAz3Nh")
auth.set_access_token("3530340917-urj3UuRWL6frj2FtdhQjj6v0PpVF0PoJy6hp6og", 
	"eW9ZyEZID417pFtZDTLwUI95u60TCcict290qxnBIXleE")

gmaps = googlemaps.Client(key='AIzaSyD4cKAyllPW6joKXP52BUlJdglliTsgTSg')
api = tweepy.API(auth)

# Getting the first batch
batch = api.search("#FakeTears", count=100)
oldest = batch[-1].id-1

tweets = {}
collect = True
# Open the json file and keep adding the tweets
with open("fake_tears_1000.json", "w") as f:
	while(collect):
		if(!collect): break
		for tweet in batch:
			if(len(tweet) == 700):
				collect = False
				break
			print(len(tweets))
			address = tweet.user.location
			text = tweet.text
			if(address): tweets[text] = address
		batch = api.search("#FakeTears", count=100, max_id=oldest)
		oldest = batch[-1].id-1

	json.dump(tweets, f)
