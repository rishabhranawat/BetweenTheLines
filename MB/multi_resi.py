import tweepy
import json
import pprint
import googlemaps

from multiprocessing.dummy import Pool as ThreadPool 

class TryMulti():
	gmaps = googlemaps.Client(key='AIzaSyD4cKAyllPW6joKXP52BUlJdglliTsgTSg')
	data = {}
	
	def get_state(self, tweet):
		address = tweet.user.location
		location = self.gmaps.geocode(address)
		if(location):
			c = location[0]['address_components']
			for l in c:
				if("administrative_area_level_1" in l['types']):
					state = l['long_name']
					try:
						self.data[state] += 1 
					except:
						self.data[state] = 1
					return state
		return None

	def main(self):
		auth = tweepy.OAuthHandler("7ORmqhp1lXxpazSzpTGVVNAv6", "KXwjMsUcf0cKLIZ94D76GYwJeAhQ2qbUlxp2OnENVDQXIAz3Nh")
		auth.set_access_token("3530340917-urj3UuRWL6frj2FtdhQjj6v0PpVF0PoJy6hp6og", "eW9ZyEZID417pFtZDTLwUI95u60TCcict290qxnBIXleE")
		api = tweepy.API(auth)

		batch = api.search("#FakeTears", count=100)
		oldest = batch[-1].id-1
		tweets = []
		count = 0

		for tweet in batch:
			count += 1
			address = tweet.user.location
			if(address):
				tweets.append(tweet)

		pool = ThreadPool(4) 
		results = pool.map(my_function, my_array)

