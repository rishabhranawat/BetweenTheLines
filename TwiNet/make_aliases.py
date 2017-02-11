import json
import tweepy

# Twitter Auth
auth = tweepy.OAuthHandler("7ORmqhp1lXxpazSzpTGVVNAv6", 
	"KXwjMsUcf0cKLIZ94D76GYwJeAhQ2qbUlxp2OnENVDQXIAz3Nh")
auth.set_access_token("3530340917-urj3UuRWL6frj2FtdhQjj6v0PpVF0PoJy6hp6og", 
	"eW9ZyEZID417pFtZDTLwUI95u60TCcict290qxnBIXleE")
api = tweepy.API(auth)

with open("bin/heads_of_states_100.json") as f:
	heads = json.load(f)
f.close()

with open("list.json") as f:
	handles = json.load(f)
f.close()

alias = {}

for country, screen_name in handles.items():
	try:
		# Get head title
		head = heads[country].replace("\u2013", "")
		title_head = head.replace("  ", " ").strip()
		head = head.\
		replace("President", "").\
		replace("Prime Minister", "").\
		replace("Supreme Leader", "").\
		replace("Prince", "").\
		replace("Federal Chancellor", "").\
		replace("of the Government", "").strip()
		
		# get location in a list
		user = api.get_user(screen_name)
		location = user.location.split(",")
		
		# get data
		data = [screen_name, title_head, head, country]
		data.extend(head.split(" "))
		data.extend(location)

		alias[country] = [x.lower() for x in list(set(data))]
	except:
		print(country)

with open("aliases.json", "w") as f:
	json.dump(alias, f)