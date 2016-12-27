from urllib import *
from lxml import html
import requests, json
from urllib.request import Request, urlopen
import facebook

class FacebookGoogleAggregator():
	# API DETAILS
	APP_ID = "1254942267860327"
	API_KEY = "b41369a7ec1e753a7274e752afc8b9a4"

	def get_verified_id(self, page_results):
		for each in page_results:
			if(each['is_verified']):
				return each['id']

	def getYouTubeDetails(self):
		
		# Source of the top youtube channels - vistatsx.com
		# url = "http://vidstatsx.com/youtube-top-100-most-subscribed-channels"
		url = "http://vidstatsx.com/youtube-top-200-most-subscribed-channels"
		req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
		page = html.fromstring(urlopen(req).read())
		el = page.xpath("//a[@class='user']")

		youtube_channel_details = {}
		for each in el:
			if(each.text[0] != "#"):
				youtube_channel_details[each.text] = each.attrib["href"].replace("/youtube-channel", "")
		return youtube_channel_details

	def getFacebookFromTopYouTubeChannels(self, youtube_channel_details):
		
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

	def getFirstLevelData(self):
		youtube_channel_details = self.getYouTubeDetails()
		print(self.getFacebookFromTopYouTubeChannels(youtube_channel_details))


a = FacebookGoogleAggregator()
a.getFirstLevelData()



# url = "https://graph.facebook.com/v2.8/10154804184463896/video_insights/total_video_views_unique&access_token="+access_token
# print(requests.get(url).json())