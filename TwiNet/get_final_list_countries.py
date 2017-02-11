import tweepy
import pickle
import googlemaps
import csv
import json


# helper functions

# get nations with high GDP
def get_nations():
	nations = []
	with open('bin/top_100_countries.csv', 'r') as csvfile:
		spamreader = csv.reader(csvfile)
		for row in spamreader:
			nations.extend(row)
	return nations

# get cleaned nations
def get_cleaned_collected():
	with open("twitter_handle_with_nations.json") as f:
		collected = json.load(f)
	f.close()
	nations = get_nations()
	collectedf = {}
	for country, screen_name in collected.items():
		if(country in nations):
			collectedf[country] = screen_name
	return collectedf

# with open("bin/heads_of_states_100.json") as f:
# 	heads = json.load(f)


# # Twitter Auth
# auth = tweepy.OAuthHandler("7ORmqhp1lXxpazSzpTGVVNAv6", 
# 	"KXwjMsUcf0cKLIZ94D76GYwJeAhQ2qbUlxp2OnENVDQXIAz3Nh")
# auth.set_access_token("3530340917-urj3UuRWL6frj2FtdhQjj6v0PpVF0PoJy6hp6og", 
# 	"eW9ZyEZID417pFtZDTLwUI95u60TCcict290qxnBIXleE")
# api = tweepy.API(auth)

# # Figure out a way to get the best 100
# collectedf = get_cleaned_collected()
# for country, screen_name in collectedf.items():
# 	if(screen_name == None):
# 		value = heads[country].replace("\u2013", "-")
# 		word = country+" "+value.split("-")[0]
# 		print(word)
# 		users = api.search_users(word)
# 		for each in users:
# 			if(each.verified):
# 				print(each.screen_name)
# 		entered_name = input(country+" Enter twitter handle without @: ")
# 		if(entered_name != "d"):
# 			collectedf[country] = entered_name

# print(collectedf)
# with open("list.json", "w") as f:
# 	json.dump(collectedf, f)
# f.close()


data = get_cleaned_collected()
d = {}
count = 0
for key, value in data.items():
	if(value):
		count += 1
		d[key] = value

print(count)

with open("list.json", "w") as f:
	json.dump(d, f)