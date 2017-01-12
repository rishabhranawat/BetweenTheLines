import requests, json

from lxml import html
from urllib import *
from urllib.request import Request, urlopen

import csv


def get_vevo_channels():
	url = "http://vidstatsx.com/youtube-top-500-most-subscribed-channels"
	req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
	page = html.fromstring(urlopen(req).read())
	el = page.xpath("//a[@class='user']")

	youtube_channel_details = {}
	for each in el:
		if("VEVO" in each.text.upper()):
			youtube_channel_details[each.text] = each.attrib["href"].replace("/youtube-channel", "")
	
	print("ALL VEVO YOUTUBE CHANNELS IN TOP 100")
	print(youtube_channel_details, len(youtube_channel_details))
	return youtube_channel_details

def get_verified_id(page_results):
	for each in page_results:
		if(each['is_verified']):
			return each['id']
def get_facebook_youtube_from_youtube():
	APP_ID = "1254942267860327"
	API_KEY = "b41369a7ec1e753a7274e752afc8b9a4"
	
	youtube_channel_details = get_vevo_channels()

	# Get Authentication access to facebook's graph API
	url = "https://graph.facebook.com/oauth/access_token?grant_type=client_credentials&read_insights&client_id="+APP_ID+"&client_secret="+API_KEY
	access_token = requests.get(url).text.replace("access_token=", "")

	# Get corresponding verified channels to the top 200 youtube channels in youtube_channel_details
	all_channels_details = {}
	for key, value in youtube_channel_details.items():
		r_url = "https://graph.facebook.com/v2.8/search?type=page&q="+key+"&fields=is_verified&access_token="+access_token
		page_details = requests.get(r_url).json()
		page_results = page_details['data']
		
		verified_id = get_verified_id(page_results)
		if(verified_id):
			all_channels_details[key] = [verified_id, value]
	
	print("CORRESPONDING VERIFIED FACEBOOK PAGES")
	print(all_channels_details, len(all_channels_details))
	return all_channels_details


def get_vevo_lens():

	APP_ID = "1254942267860327"
	API_KEY = "b41369a7ec1e753a7274e752afc8b9a4"
	all_channels = {'Vevo': ['79544810932', '/Vevo']}

	url = "https://graph.facebook.com/oauth/access_token?grant_type=client_credentials&read_insights&client_id="+APP_ID+"&client_secret="+API_KEY
	access_token = requests.get(url).text.replace("access_token=", "")

	for key, value in all_channels.items():
		r_url = "https://graph.facebook.com/v2.8/"+value[0]+"/videos?fields=title,description,length&access_token="+access_token
		videos = requests.get(r_url).json()
		results = videos['data']
		all_facebook_videos = results
	
	with open("vevo_youtube_facebook.csv", "w") as f:
		writer = csv.writer(f)

		for each in all_facebook_videos:
			writer.writerow([each["description"], each["length"]])
	



get_vevo_lens()