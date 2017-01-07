# fga module - FacebookGoogleAggregator - Aggregates the top 200 youtube channels
# with their corresponding facebook pages

import requests, json

from lxml import html
from urllib import *
from urllib.request import Request, urlopen

import facebook

class fga():
	# API DETAILS
	APP_ID = "1254942267860327"
	API_KEY = "b41369a7ec1e753a7274e752afc8b9a4"

	def get_verified_id(self, page_results):
		for each in page_results:
			if(each['is_verified']):
				return each['id']

	def get_youtube_detail(self):
		
		# Source of the top youtube channels - vistatsx.com
		# url = "http://vidstatsx.com/youtube-top-100-most-subscribed-channels"
		url = "http://vidstatsx.com/youtube-top-500-most-subscribed-channels"
		req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
		page = html.fromstring(urlopen(req).read())
		el = page.xpath("//a[@class='user']")

		youtube_channel_details = {}
		for each in el:
			if(each.text[0] != "#"):
				youtube_channel_details[each.text] = each.attrib["href"].replace("/youtube-channel", "")

		url = "http://vidstatsx.com/youtube-top-200-most-subscribed-channels"
		req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
		page = html.fromstring(urlopen(req).read())
		el = page.xpath("//a[@class='user']")

		for each in el:
			if(each.text[0] != "#"):
				youtube_channel_details[each.text] = each.attrib["href"].replace("/youtube-channel", "")

		return youtube_channel_details

	def get_facebook_youtube_from_youtube(self, youtube_channel_details):
		
		# Get Authentication access to facebook's graph API
		url = "https://graph.facebook.com/oauth/access_token?grant_type=client_credentials&read_insights&client_id="+self.APP_ID+"&client_secret="+self.API_KEY
		access_token = requests.get(url).text.replace("access_token=", "")

		# Get corresponding verified channels to the top 200 youtube channels in youtube_channel_details
		all_channels_details = {}
		for key, value in youtube_channel_details.items():
			r_url = "https://graph.facebook.com/v2.8/search?type=page&q="+key+"&fields=is_verified&access_token="+access_token
			page_details = requests.get(r_url).json()
			page_results = page_details['data']
			
			verified_id = self.get_verified_id(page_results)
			if(verified_id):
				all_channels_details[key] = [verified_id, value]
		
		return all_channels_details

	def get_first_level_data(self):
		youtube_channel_details = self.get_youtube_detail()
		all_valid_channels = self.get_facebook_youtube_from_youtube(youtube_channel_details)

		with open('channel_detail.json', 'w') as fp:
			json.dump(all_valid_channels, fp)

		return all_valid_channels

	def get_facebook_video_titles(self):
		url = "https://graph.facebook.com/oauth/access_token?grant_type=client_credentials&read_insights&client_id="+self.APP_ID+"&client_secret="+self.API_KEY
		access_token = requests.get(url).text.replace("access_token=", "")

		r_url = "https://graph.facebook.com/v2.8/FallonTonight/videos&access_token="+access_token
		with open("channel_detail.json") as data_file:
			all_channels = json.load(data_file)

		all_facebook_videos = {}
		for key, value in all_channels.items():
			r_url = "https://graph.facebook.com/v2.8/"+value[0]+"/videos?fields=title,description&access_token="+access_token
			videos = requests.get(r_url).json()
			results = videos['data']
			
			all_facebook_videos[key] = []

			for each in results:
				try:
					title_val = each["title"]
					if(title_val == "" or title_val == None):
						all_facebook_videos[key].append({each["description"] : each["id"]})
					else:
						all_facebook_videos[key].append({each["title"] : each["id"]})
				except KeyError as e:
					print(e)
					pass
		
		with open("facbeook_video_title_id.json", "w") as fvti:
			json.dump(all_facebook_videos, fvti)

	def get_facebook_to_google_video_titles(self):
		url = "https://graph.facebook.com/oauth/access_token?grant_type=client_credentials&read_insights&client_id="+self.APP_ID+"&client_secret="+self.API_KEY
		access_token = requests.get(url).text.replace("access_token=", "")

		r_url = "https://graph.facebook.com/v2.8/FallonTonight/videos&access_token="+access_token
		with open("channel_detail.json") as data_file:
			all_channels = json.load(data_file)

		all_facebook_videos = {}
		for key, value in all_channels.items():
			r_url = "https://graph.facebook.com/v2.8/"+value[0]+"/videos?limit=10&fields=title,description&access_token="+access_token
			videos = requests.get(r_url).json()
			results = videos['data']
			
			all_facebook_videos[key] = []

			for each in results:
				try:
					title_val = each["title"]
					if(title_val == "" or title_val == None):
						all_facebook_videos[key].append({each["description"] : each["id"]})
					else:
						all_facebook_videos[key].append({each["title"] : each["id"]})
				except KeyError as e:
					pass
		
		with open("facebook_to_google_fb_vids.json", "w") as fvti:
			json.dump(all_facebook_videos, fvti)

	def get_google_videos(self):
		with open("channel_detail.json") as data_file:
			all_channels = json.load(data_file)
		
		vals = all_channels
		all_vids = {}

		for key, val in vals.items():
				
				# Get all google videos
			try:
				name = val[1]
				url = "https://www.googleapis.com/youtube/v3/channels?part=contentDetails&forUsername="+name.replace("/", "")+"&key=AIzaSyBxuVNgsVOm3GVeIsyrYK1KvyKyWFXY2q8"
				channel_data = json.loads(requests.get(url).text)
				uploads_id = channel_data['items'][0]['contentDetails']['relatedPlaylists']['uploads']
				k_url = "https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=10&playlistId="+uploads_id+"&key=AIzaSyBxuVNgsVOm3GVeIsyrYK1KvyKyWFXY2q8"
				videos_data = json.loads(requests.get(k_url).text)
				items = videos_data['items']
				all_vids[key] = items
			except:
				all_vids[key] = []

		with open("google_video_lists_10.json", "w") as fv:
			json.dump(all_vids, fv)

a = fga()
# a.get_first_level_data()
# a.get_facebook_video_titles()	
# a.get_facebook_to_google_video_titles()
a.get_google_videos()
