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
batch = api.search("#deleteuber", count=100)
oldest = batch[-1].id-1

tweets = {}
count = 0

while(count < 2000):
	for tweet in batch:
		address = tweet.user.location
		text = tweet.text
		if(address):
			count += 1 
			tweets[text] = address
			print(count, tweet.id)
	batch = api.search("#deleteuber", count=100, max_id=oldest)
	oldest = batch[-1].id-1

with open("delete_uber_max.json", "w") as f:
	json.dump(tweets, f)