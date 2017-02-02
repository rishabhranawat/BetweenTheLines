import tweepy
import json
import pprint
import time

# Twitter authorization
auth = tweepy.OAuthHandler("7ORmqhp1lXxpazSzpTGVVNAv6", 
	"KXwjMsUcf0cKLIZ94D76GYwJeAhQ2qbUlxp2OnENVDQXIAz3Nh")
auth.set_access_token("3530340917-urj3UuRWL6frj2FtdhQjj6v0PpVF0PoJy6hp6og", 
	"eW9ZyEZID417pFtZDTLwUI95u60TCcict290qxnBIXleE")
api = tweepy.API(auth)

# Getting the first batch
batch = api.search("#BoycottStarbucks", count=100)
oldest = batch[-1].id-1

tweets = {}
count = 0

# Open the json file and keep adding the tweets
try:
	with open("boycott_starbucks_1000.json", "w") as f:
		while(count < 1000):
			for tweet in batch:
				count += 1
				print(count)
				address = tweet.user.location
				text = tweet.text
				if(address): tweets[text] = address
			batch = api.search("#BoycottStarbucks", count=100, max_id=oldest)
			oldest = batch[-1].id-1
		json.dump(tweets, f)
except Exception as e:
	json.dump(tweets, f)