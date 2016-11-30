import facebook
from urllib import *
from lxml import html
import requests
import json

APP_ID = "1254942267860327"
API_KEY = "b41369a7ec1e753a7274e752afc8b9a4"
access_token = "EAACEdEose0cBALOaIXELFQxvVflf9ZANUR6eJefdLMJKSYDIinNJUovKZC73CuJNTglMbgzzmj0ZBQrs1zZAvTAFWDSSkEzsr4lCtvZAtwKTJovKgtojp7DYpiHDyoRDrfSkTBJZBa7hr9CYfVoElHHDRjz2PBaaetq67HMZBmjAwZDZD"
graph = facebook.GraphAPI(access_token=access_token, version = "2.7")


# videos = graph.get(path = 'v2.8/FallonTonight/videos')["data"]
# video_ids = []
# for video in videos:
# 	video_ids.append(video["id"])

# print(video_ids)
# for each_id in video_ids:
# 	url = "https://www.facebook.com/FallonTonight/videos/"+each_id+"/"
# 	page = html.fromstring(request.urlopen(url).read())
# 	print(page.xpath("//span")[0].text)
# 	el = page.xpath("//span[@class='fcg']")


# Figured out a way to find the best VERIFIED way to get the facebook pages and thus, their 
# corresponding details
# DEVELOPER_KEY = "AIzaSyBxuVNgsVOm3GVeIsyrYK1KvyKyWFXY2q8"
# CSE_KEY = urllib.parse.quote("010574959533657678901:wcpwn5hwe-k")
# url = "https://www.googleapis.com/customsearch/v1?q=fallon&cx="+CSE_KEY+"&key="+DEVELOPER_KEY
# requests.get(url)

url = "https://graph.facebook.com/oauth/access_token?grant_type=client_credentials&client_id=1254942267860327&client_secret=b41369a7ec1e753a7274e752afc8b9a4"
access_token = requests.get(url).text.replace("access_token=", "")

r_url = "https://graph.facebook.com/v2.8/search?type=page&q=boyceavenue&fields=is_verified&access_token="+access_token
data = requests.get(r_url).json