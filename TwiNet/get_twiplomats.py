import tweepy
import pickle
import googlemaps
import csv
import json

# Twitter Auth
auth = tweepy.OAuthHandler("7ORmqhp1lXxpazSzpTGVVNAv6", 
	"KXwjMsUcf0cKLIZ94D76GYwJeAhQ2qbUlxp2OnENVDQXIAz3Nh")
auth.set_access_token("3530340917-urj3UuRWL6frj2FtdhQjj6v0PpVF0PoJy6hp6og", 
	"eW9ZyEZID417pFtZDTLwUI95u60TCcict290qxnBIXleE")
api = tweepy.API(auth)

# Collect twiplomats
twiplomats = []
x = api.list_timeline("Twiplomacy", "world-leaders", count=100)
twiplomats.extend(x)
old_id = x[-1].id
count = 100
while(count <= 500):
	print("Twiplomats!", count)
	more = api.list_timeline("Twiplomacy", "world-leaders", count=100, max_id=old_id)
	twiplomats.extend(more)
	old_id = more[-1].id
	count += 100

actual_data = {}
for tw in twiplomats:
	user = None
	location = None
	try:
		user = tw.user
		try:
			location = user.location
		except:
			try:
				location = tw.location
			except:
				pass
	except:
		pass

	if(location and user):
		actual_data[user.screen_name] = location

with open("twiplomats_accounts_3.json", "w") as f:
	json.dump(actual_data, f)

