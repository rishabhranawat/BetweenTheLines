# @author - Rishabh Ranawat for BetweenTheLines
# Gets the top youtube channels with their usernames
# Outputs a separate file with the youtube names

import requests, json
from lxml import html
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

		with open("facebook_to_google_fb_vids.json") as fv:
			facebook_videos = json.load(fv)

		with open("google_video_lists.json") as fv1:
			google_videos = json.load(fv1)

		data = {}
		
		vals = self.valid_channels
		count = 0

		with open("trial_all_fb_youtube.csv", "w") as f:
			writer = csv.writer(f)
			for key, val in vals.items():
				
				# Get all fb videos
				all_fb_vids = facebook_videos[key]
				all_google_videos = google_videos[key]

				try: a = data[key]
				except: data[key] = {}

				for vids in all_fb_vids:
					for fb_title, value in vids.items():
						
						max_rat = -1
						max_title = None
						max_id = None

						for each in all_google_videos:
							video_id = each['snippet']['resourceId']['videoId']
							v_url = "https://www.googleapis.com/youtube/v3/videos?part=statistics&id="+video_id+"&key=AIzaSyBxuVNgsVOm3GVeIsyrYK1KvyKyWFXY2q8"
							details = json.loads(requests.get(v_url).text)
							title = each['snippet']['title']
							google_view_count = details['items'][0]['statistics']['viewCount']

							title_rat = fuzz.ratio(fb_title, title)
							if(title_rat > max_rat):
								max_rat = title_rat
								max_title = fb_title
								max_id = value


							if(max_rat > 90):
								count += 1
								print(max_title, title, count)
								url = "https://www.facebook.com/"+val[0]+"/videos/"+max_id
								driver.get(url)
								try:
									facebook_view_count = driver.find_element_by_class_name("_1t6k").text
									data[key][title] = {"fb": facebook_view_count, "google": google_view_count}
									writer.writerow([key, title, google_view_count, facebook_view_count])
								except:
									print("Unexpected Error 1")
									pass
							else:
								count += 1
								try:
									facebook_view_count = driver.find_element_by_class_name("_1t6k").text
									data[key][title] = {"fb": facebook_view_count, "google": 0}
									writer.writerow([key, title, 0, facebook_view_count])
								except:
									print("Unexpected Error 2")
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

with open("trial_4.csv", "w") as f:
	writer = csv.writer(f)

	for key, value in all_data.items():
		for title, views in value.items():
			writer.writerow([key, title, views["google"], views["fb"]])