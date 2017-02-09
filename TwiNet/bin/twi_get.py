import tweepy
import json
import pprint

auth = tweepy.OAuthHandler("7ORmqhp1lXxpazSzpTGVVNAv6", "KXwjMsUcf0cKLIZ94D76GYwJeAhQ2qbUlxp2OnENVDQXIAz3Nh")
auth.set_access_token("3530340917-urj3UuRWL6frj2FtdhQjj6v0PpVF0PoJy6hp6og", "eW9ZyEZID417pFtZDTLwUI95u60TCcict290qxnBIXleE")

api = tweepy.API(auth)

# with open("heads_of_states_100.json") as f:
# 	heads = json.load(f)

# heads_twitter = {}
# for key, value in heads.items():
# 	value = value.replace("\u2013", "-")
# 	word = key+" "+value.split("-")[0]
# 	print(word)
# 	users = api.search_users(word)
# 	for u in users:
# 		if(u.verified):
# 			heads_twitter[key] = [value, u.screen_name]
# 			break

# print(len(heads_twitter))
# pp = pprint.PrettyPrinter(indent=4)
# pp.pprint(heads_twitter)

# with open("heads_twitter_100.json", "w") as f:
# 	json.dump(heads_twitter, f)


with open("heads_twitter_100.json") as f:
	heads_twitter = json.load(f)

state_tweets = {}

for key, value in heads_twitter.items():
	leader = value[0]
	screen_name = value[1]
	state = key

	tweets = api.user_timeline(screen_name, count=200)
	oldest = tweets[-1].id - 1
	count = 200
	while(count < 1000):
		print(count)
		statuses = api.user_timeline(screen_name, count = 200, max_id=oldest)
		if(len(statuses) > 0):
			tweets.extend(statuses)
			oldest = statuses[-1].id-1
			count += 200
		else:
			break

	all_tweets = []
	for each in tweets: 
		all_tweets.append(each.text)

	state_tweets[key] = all_tweets
	print(all_tweets)

with open("all_tweets.json", "w") as f:
	json.dump(state_tweets, f)

