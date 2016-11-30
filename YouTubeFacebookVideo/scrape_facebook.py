import facebook
from urllib import *
from lxml import html
import requests
import json

with open("youtube_channels.json") as data_file:
	data = json.load(data_file)

APP_ID = "1254942267860327"
API_KEY = "b41369a7ec1e753a7274e752afc8b9a4"

url = "https://graph.facebook.com/oauth/access_token?grant_type=client_credentials&client_id="+APP_ID+"&client_secret="+API_KEY
access_token = requests.get(url).text.replace("access_token=", "")

count = 0
for key, value in data.items():
	if(count > 1): break
	key = "boyceavenue"
	r_url = "https://graph.facebook.com/v2.8/search?type=page&q="+key+"&fields=is_verified&access_token="+access_token
	page_details = requests.get(r_url).json()
	page_results = page_details['data']
	for each in page_results:
		if(each['is_verified']):
			print(key+" "+each['id'])
			break
	count += 1
