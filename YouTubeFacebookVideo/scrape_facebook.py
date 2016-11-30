import facebook
from urllib import *
from lxml import html
import requests
import json

APP_ID = "1254942267860327"
API_KEY = "b41369a7ec1e753a7274e752afc8b9a4"

def get_verified_id(page_results):
	for each in page_results:
		if(each['is_verified']):
			return each['id']

with open("youtube_channels.json") as data_file:
	data = json.load(data_file)

url = "https://graph.facebook.com/oauth/access_token?grant_type=client_credentials&client_id="+APP_ID+"&client_secret="+API_KEY
access_token = requests.get(url).text.replace("access_token=", "")

verified_ids_count = 0
data_with_ids = {}
for key, value in data.items():
	r_url = "https://graph.facebook.com/v2.8/search?type=page&q="+key+"&fields=is_verified&access_token="+access_token
	page_details = requests.get(r_url).json()
	page_results = page_details['data']
	
	verified_id = get_verified_id(page_results)
	if(verified_id):
		verified_ids_count += 1
		data_with_ids[key] = [verified_id, value]
		print(key, data_with_ids[key])

with open("facebook_page.json", 'w') as write_data_file:
	write_data_file.write(json.dumps(data_with_ids, indent=4))

