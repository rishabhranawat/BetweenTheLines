import tweepy
import json
import pprint
from geopy.geocoders import Nominatim


class MultiThreadedCollection():

	tweets = []
	
	def main(self):
		geolocator = Nominatim()

		auth = tweepy.OAuthHandler("7ORmqhp1lXxpazSzpTGVVNAv6", "KXwjMsUcf0cKLIZ94D76GYwJeAhQ2qbUlxp2OnENVDQXIAz3Nh")
		auth.set_access_token("3530340917-urj3UuRWL6frj2FtdhQjj6v0PpVF0PoJy6hp6og", "eW9ZyEZID417pFtZDTLwUI95u60TCcict290qxnBIXleE")

		api = tweepy.API(auth)

		batch = api.search("#FakeTears", count=100)
		oldest = batch[-1].id-1

		tweets = self.tweets
		count = 0
		while(len(batch) > 0):
			for tweet in batch:
				count += 1
				tweets.append(tweet)
			batch = api.search("#Resist", count=100, max_id=oldest)
			oldest = batch[-1].id-1

		with open('outfile', 'wb') as fp:
		    pickle.dump(tweets, fp)

	def collect(self, batch):
			for tweet in batch:
		count += 1
		print(count)
		address = tweet.user.location

		if(address != None and address != ""):
			try:
				location = geolocator.geocode(address, addressdetails=True)
				state = location.raw["address"]["state"]
				print(state, count)
				try:
					tweets[state].append(tweet)
				except:
					tweets[state] = [tweet]
			except: 
				pass





x()

with open("resist_tweets.json", "w") as f:
	json.dump(tweets, f)