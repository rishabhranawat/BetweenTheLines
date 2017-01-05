# @author - Rishabh Ranawat for BetweenTheLines
# Gets the top youtube channels with their usernames
# Outputs a separate file with the youtube names

import requests, json
from urllib.request import Request, urlopen
from lxml import html
from fga import fga as fga
from fuzzywuzzy import fuzz
import sys
import csv

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class fgda():
	valid_channels = {}
	facebook_videos = {}

	def get_valid_channels(self):
		with open("channel_detail.json") as data_file:
			all_channels = json.load(data_file)
		self.valid_channels = all_channels

	def get_facebook_videos(self):
		with open("facbeook_video_title_id.json") as data_file:
			data = json.load(data_file)
		self.facebook_videos = data

	def  get_data(self):

		driver = webdriver.Firefox()
		driver.get("https://www.facebook.com")

		email = driver.find_element_by_id("email")
		email.send_keys("rishabhranawat@yahoo.com")

		password = driver.find_element_by_id("pass")
		password.send_keys("zinnialondon!!")

		button = driver.find_element_by_id("loginbutton")
		button.click()


		data = {}
		vals = self.valid_channels

		for key, val in vals.items():
			try:
				name = val[1]
				url = "https://www.googleapis.com/youtube/v3/channels?part=contentDetails&forUsername="+name.replace("/", "")+"&key=AIzaSyBxuVNgsVOm3GVeIsyrYK1KvyKyWFXY2q8"
				channel_data = json.loads(requests.get(url).text)
				uploads_id = channel_data['items'][0]['contentDetails']['relatedPlaylists']['uploads']
				k_url = "https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=50&playlistId="+uploads_id+"&key=AIzaSyBxuVNgsVOm3GVeIsyrYK1KvyKyWFXY2q8"
				videos_data = json.loads(requests.get(k_url).text)
				items = videos_data['items']
				for each in items:
					video_id = each['snippet']['resourceId']['videoId']
					v_url = "https://www.googleapis.com/youtube/v3/videos?part=statistics&id="+video_id+"&key=AIzaSyBxuVNgsVOm3GVeIsyrYK1KvyKyWFXY2q8"
					details = json.loads(requests.get(v_url).text)
					title = each['snippet']['title']
					google_view_count = details['items'][0]['statistics']['viewCount']

					# All facebook videos for the channel

					found = False
					fb_vids = self.facebook_videos[key]
					try:
						a = data[key] 
					except:
						data[key] = {}
					for vids in fb_vids:
						if(found == False):
							for fb_title, value in vids.items():
								if(fuzz.ratio(fb_title, title) > 80):
									print(fb_title, title)
									found = True
									url = "https://www.facebook.com/"+val[0]+"/videos/"+value
									driver.get(url)
									try:
										facebook_view_count = driver.find_element_by_class_name("_1t6k").text
										data[key][title] = {"fb": facebook_view_count, "google": google_view_count}
									except:
										pass
						else:
							found = False
							break
			except:
				pass
		return data


fgda = fgda()
fgda.get_valid_channels()
fgda.get_facebook_videos()


data = fgda.get_data()

with open('comparison_data.json', 'w') as fp:
	json.dump(data, fp)

with open("comparison_data.json") as fp:
	all_data = json.load(fp)

with open("trial_3.csv", "w") as f:
	writer = csv.writer(f)

	for key, value in all_data.items():
		for title, views in value.items():
			writer.writerow([key, title, views["google"], views["fb"]])