import json
from alchemyapi import AlchemyAPI

a = AlchemyAPI()

with open("deeper_dive/mentions_tweets_mofo_count.json") as f:
	tweets = json.load(f)
f.close()

def get_mentions_structure(nat):
	mentions = {}
	for country, details in nat.items():
		mentions[country] = {}
		for c1, details in nat.items():
			if c1 != country: mentions[country][c1] = []
	return mentions

data = get_mentions_structure(tweets)

for country, details in tweets.items():
	for c1, tweets in details.items():
		for tweet in tweets:
			try:
				resp = a.sentiment('text', tweet, {'sentiment':1})
				if(resp['type'] == '')
				data[country][c1].append(resp['docSentiment']['score'])
			except:
				pass

print(data)
with open("sentiment_tweets_data.json", "w") as f:
	json.dump(data, f)
f.close()
