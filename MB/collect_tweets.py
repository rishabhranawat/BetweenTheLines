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

auth = tweepy.OAuthHandler("7ORmqhp1lXxpazSzpTGVVNAv6", "KXwjMsUcf0cKLIZ94D76GYwJeAhQ2qbUlxp2OnENVDQXIAz3Nh")
auth.set_access_token("3530340917-urj3UuRWL6frj2FtdhQjj6v0PpVF0PoJy6hp6og", "eW9ZyEZID417pFtZDTLwUI95u60TCcict290qxnBIXleE")
gmaps = googlemaps.Client(key='AIzaSyD4cKAyllPW6joKXP52BUlJdglliTsgTSg')
api = tweepy.API(auth)

batch = api.search("#FakeTears", count=100)
oldest = batch[-1].id-1
tweets = {}
count = 0
while(len(batch) > 0):
	for tweet in batch:
		count += 1
		address = tweet.user.location
		if(address):
			location = gmaps.geocode(address)
			if(location):
				state = get_state(location)
				print(count, state)
				if(state):
					try:
						tweets[state].append(tweet)
					except:
						tweets[state] = [tweet]

	batch = api.search("#FakeTears", count=100, max_id=oldest)
	oldest = batch[-1].id-1

with open("resist_tweets.json", "w") as f:
	json.dump(tweets, f)

