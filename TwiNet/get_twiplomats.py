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

# Google maps Auth
gmaps = googlemaps.Client(key='AIzaSyDOVRlWChH9IbHnR1raF2sjNDvtAe24R04')

# Get countries by highest GDPs
nations = []
with open('bin/top_100_countries.csv', 'r') as csvfile:
	spamreader = csv.reader(csvfile)
	for row in spamreader:
		nations.extend(row)

# Collect twiplomats
twiplomats = []
x = api.list_timeline("Twiplomacy", "world-leaders", count=100)
twiplomats.extend(x)
old_id = x[-1].id-1
count = 100
while(count <= 500):
	print("Twiplomats!", count)
	more = api.list_timeline("Twiplomacy", "world-leaders", count=100, 
		max_id=old_id)
	twiplomats.extend(more)
	old_id = more[-1].id-1
	count += 100

actual_data = {}
for tw in twiplomats:
	try:
		user = tw.user
		actual_data[user.screen_name] = [location]
	except:
		pass

with open("twiplomats_accounts.json", "w") as f:
	json.dump(actual_data, f)


# def get_country(location):
# 	c = location[0]['address_components']
# 	for l in c:
# 		if("country" in l['types']):
# 			return l['long_name']
# 	return None

# data = {}
# aux = {}
# for nation in nations: data[nation] = []

# for twiplomat in twiplomats:
# 	if(twiplomat.user.location): 
# 		location = gmaps.geocode(twiplomat.user.location)
# 		if(location):
# 			country = get_country(location)
# 			if(country):
# 				try:
# 					data[country].extend([twiplomat.user.id, 
# 						twiplomat.user.screen_name, twiplomat.user.location])
# 				except:
# 					try:
# 						aux[country].extend([twiplomat.user.id, 
# 						twiplomat.user.screen_name, twiplomat.user.location])
# 					except:
# 						aux[country] = [twiplomat.user.id, 
# 						twiplomat.user.screen_name, twiplomat.user.location]

# with open("twiplomats_handles.json") as g:
# 	json.dump(data, g)

# with open("aux_handles.json") as h:
# 	json.dump(aux, h)
