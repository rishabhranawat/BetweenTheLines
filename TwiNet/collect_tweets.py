import json
import tweepy
import sys

batch = "batch_"+str(sys.argv[1])
with open(batch+".json") as f:
	data = json.load(f)
f.close()

# Twitter Auth
auth = tweepy.OAuthHandler("7ORmqhp1lXxpazSzpTGVVNAv6", 
	"KXwjMsUcf0cKLIZ94D76GYwJeAhQ2qbUlxp2OnENVDQXIAz3Nh")
auth.set_access_token("3530340917-urj3UuRWL6frj2FtdhQjj6v0PpVF0PoJy6hp6og", 
	"eW9ZyEZID417pFtZDTLwUI95u60TCcict290qxnBIXleE")
api = tweepy.API(auth)

def get_500_tweets(api, screen_name):
	tweets = []
	x = api.user_timeline(screen_name, count=200)
	old_id = x[-1].id-1
	ids = set()
	while(len(tweets) <= 500 and len(x) > 0):
		for each in x:
			if(each.id not in ids):
				ids.add(each.id)
				tweets.append(each.text)
		x = api.user_timeline(screen_name, count=200, max_id=old_id)
		if(len(x) > 0):
			old_id = x[-1].id-1
	return [tweets, old_id]

final_data = {}
old_ids = {}
for country, screen_name in data.items():
	k = get_500_tweets(api, screen_name)
	tweets = k[0]
	print(screen_name, len(tweets))
	old_ids[country] = [screen_name, k[1]]
	final_data[country] = [screen_name, tweets]

with open(batch+"_old_id.json", "w") as g:
	json.dump(old_ids, g)
g.close()

with open(batch+"_tweets.json", "w") as f:
	json.dump(final_data, f)
f.close()



