import json

with open("all_tweets.json") as f:
	tweets = json.load(f)


countries = ["trump", "obama","USA", "Untied States of America", "America"]
data = {}
count = 0
for key, value in tweets.items():
	data[key] = {}
	v = data[key]
	state = key
	state_tweets = value
	for tweet in state_tweets:
		print(count)
		count += 1
		for country in countries:
			if(country.lower() in tweet.lower()):
				try:
					v[country] += 1
				except:
					v[country] = 1


print(data)