import facebook
import csv
import json, requests
from urllib import *
from urllib.request import Request, urlopen

APP_ID = "1254942267860327"
API_KEY = "b41369a7ec1e753a7274e752afc8b9a4"

url = "https://graph.facebook.com/oauth/access_token?grant_type=client_credentials&read_insights&client_id="+APP_ID+"&client_secret="+API_KEY
access_token = requests.get(url).text.replace("access_token=", "")

with open("channel_detail.json") as f:
	linkers = json.load(f)

# linkers = {"PewDiePie": "193844937315070", "SciShow": "294155773949789","enchufetv":"307093412636526",
# "NoCopyrightSounds": "271354302888868", "HolaSoyGerman": "166233540126948"}

all_links = {}
with open("linkers_analysis.csv", "w") as f:
	writer = csv.writer(f)
	for key, value in linkers.items():
		all_links[key] = []
		youtube_links = 0
		r_url = "https://graph.facebook.com/v2.8/"+value[0]+"/posts?fields=link&limit=100&access_token="+access_token
		posts = requests.get(r_url).json()['data']
		print(posts)
		for each in posts:
			try:
				link = each["link"]
				if("youtube" in link or "youtu.be" in link): 
					all_links[key].append(link)
					writer.writerow([key, link])
			except:
				pass

with open("linkers_numbers.csv", "w") as f:
	writer = csv.writer(f)
	for key, value in all_links.items():
		writer.writerow([key, len(value)])
		print(key, len(value))
