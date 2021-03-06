import requests, json

from urllib.request import Request, urlopen
import facebook

import requests, json
from lxml import html
from fuzzywuzzy import fuzz
import sys
import csv

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


import isodate

def get_google_videos():
	with open("deep_dive_users.json") as f:
		vals = json.load(f)
	all_vids = {}
	for key, val in vals.items():
		name = val[1]
		url = "https://www.googleapis.com/youtube/v3/channels?part=contentDetails&forUsername="+name.replace("/", "")+"&key=AIzaSyBxuVNgsVOm3GVeIsyrYK1KvyKyWFXY2q8"
		channel_data = json.loads(requests.get(url).text)
		uploads_id = channel_data['items'][0]['contentDetails']['relatedPlaylists']['uploads']
		k_url = "https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=50&playlistId="+uploads_id+"&key=AIzaSyBxuVNgsVOm3GVeIsyrYK1KvyKyWFXY2q8"
		videos_data = json.loads(requests.get(k_url).text)
		items = videos_data['items']
		all_vids[key] = items
		
	with open("deeper_dive_google_videos.json", "w") as f:
		json.dump(all_vids, f)

def get_facebook_videos():
	APP_ID = "1254942267860327"
	API_KEY = "b41369a7ec1e753a7274e752afc8b9a4"
	with open("deep_dive_users.json") as f:
		all_channels = json.load(f)

	url = "https://graph.facebook.com/oauth/access_token?grant_type=client_credentials&read_insights&client_id="+APP_ID+"&client_secret="+API_KEY
	access_token = requests.get(url).text.replace("access_token=", "")

	all_facebook_videos = {}
	for key, value in all_channels.items():
		r_url = "https://graph.facebook.com/v2.8/"+value[0]+"/videos?fields=title,description,length&access_token="+access_token
		videos = requests.get(r_url).json()
		results = videos['data']
		
		all_facebook_videos[key] = []

		for each in results:
			try:
				all_facebook_videos[key].append({each["title"] : [each["id"], each["length"]]})
			except KeyError as e:
				try:
					all_facebook_videos[key].append({each["description"] : [each["id"], each["length"]]})
				except KeyError as e:
					print("Neither title nor description")
	with open("deeper_dive_facebook_videos.json", "w") as fvti:
		json.dump(all_facebook_videos, fvti)

def get_youtube_count(video):
	video_id = video['snippet']['resourceId']['videoId']
	title = video['snippet']['title']

	v_url = "https://www.googleapis.com/youtube/v3/videos?part=statistics&id="+video_id+"&key=AIzaSyBxuVNgsVOm3GVeIsyrYK1KvyKyWFXY2q8"
	details = json.loads(requests.get(v_url).text)
	google_view_count = details['items'][0]['statistics']['viewCount']

	return title, google_view_count

def get_youtube_duration(video):
	video_id = video['snippet']['resourceId']['videoId']

	v_url = "https://www.googleapis.com/youtube/v3/videos?part=contentDetails&id="+video_id+"&key=AIzaSyBxuVNgsVOm3GVeIsyrYK1KvyKyWFXY2q8"
	details = json.loads(requests.get(v_url).text)
	duration = details['items'][0]['contentDetails']['duration']

	return isodate.parse_duration(duration).total_seconds()

def get_facebook_home():
	driver = webdriver.Firefox()
	driver.get("https://www.facebook.com")

	email = driver.find_element_by_id("email")
	email.send_keys("rishabhranawat@yahoo.com")

	password = driver.find_element_by_id("pass")
	password.send_keys("zinnialondon!!")

	button = driver.find_element_by_id("loginbutton")
	button.click()

	return driver

def get_youtube_to_facebook():

	driver = get_facebook_home()

	with open("deep_dive_users.json") as f:
		all_channels = json.load(f)
	
	with open("deeper_dive_facebook_videos.json") as f:
		facebook_videos = json.load(f)

	with open("deeper_dive_google_videos.json") as f:
		google_videos = json.load(f)

	with open("deeper_dive_youtube_to_facebook.csv", "w") as dd:
		writer = csv.writer(dd)
		for key, value in google_videos.items():
			page_videos = facebook_videos[key]
			channel_videos = value

			for youtube_video in channel_videos:
				youtube_title, youtube_view_count = get_youtube_count(youtube_video)
				youtube_duration = get_youtube_duration(youtube_video)

				max_rat = -1
				max_title = None
				max_id = None
				max_len = None

				for facebook_video in page_videos:
					for facebook_title, facebook_details in facebook_video.items():
						title_rat = fuzz.ratio(facebook_title, youtube_title)
						if(title_rat > max_rat):
							max_rat = title_rat
							max_title = facebook_title
							max_id = facebook_details[0]
							max_len = facebook_details[1]
				if(max_rat > 90):
					print(youtube_title, max_title)
					url = "https://www.facebook.com/"+all_channels[key][0]+"/videos/"+max_id
					driver.get(url)
					try:
						facebook_view_count = driver.find_element_by_class_name("_1t6k").text
						writer.writerow([key, youtube_title, youtube_view_count, youtube_duration, facebook_view_count, max_len])
					except:
						print("Unexpected error 1")
				else:
					try:
						writer.writerow([key, youtube_title, youtube_view_count, youtube_duration, 0, 0])
					except:
						print("Unexpected Error 2")
		

def get_facebook_to_youtube():
	driver = webdriver.Firefox()
	driver.get("https://www.facebook.com")

	email = driver.find_element_by_id("email")
	email.send_keys("rishabhranawat@yahoo.com")

	password = driver.find_element_by_id("pass")
	password.send_keys("zinnialondon!!")

	button = driver.find_element_by_id("loginbutton")
	button.click()

	with open("deep_dive_users.json") as f:
		all_channels = json.load(f)
	
	with open("deeper_dive_facebook_videos.json") as f:
		facebook_videos = json.load(f)

	with open("deeper_dive_google_videos.json") as f:
		google_videos = json.load(f)

	with open("deeper_dive_facebook_to_youtube.csv", "w") as dd:
		writer = csv.writer(dd)
		for popular_name, youtube_facebook in all_channels.items():

			facebook_id = youtube_facebook[0]
			youtube_id = youtube_facebook[1]

			page_videos = facebook_videos[popular_name]
			channel_videos = google_videos[popular_name]

			for facebook_video in page_videos:
				for facebook_title, facebook_details in facebook_video.items():
					facebook_length = facebook_details[1]

					max_rat = -1
					max_title = None
					max_video = None

					for youtube_video in channel_videos:
						youtube_title = youtube_video['snippet']['title']
						title_rat = fuzz.ratio(youtube_title, facebook_title)
						if(title_rat > max_rat):
							max_rat = title_rat
							max_title = youtube_title
							max_video = youtube_video
				
				url = "https://www.facebook.com/"+facebook_id+"/videos/"+facebook_details[0]
				driver.get(url)

				try:
					facebook_view_count = driver.find_element_by_class_name("_1t6k").text
					if(max_rat > 90):
						youtube_title, youtube_view_count = get_youtube_count(max_video)
						print(youtube_title, facebook_title)
						youtube_duration = get_youtube_duration(max_video)
						writer.writerow([popular_name, facebook_title, youtube_view_count, youtube_duration, facebook_view_count, facebook_length])
					else:
						writer.writerow([popular_name, facebook_title, 0, 0, facebook_view_count, facebook_length])
				except:
					print("Unexpected Error 4")

get_facebook_to_youtube()
# get_google_videos()


