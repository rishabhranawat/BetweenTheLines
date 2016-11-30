from facepy import GraphAPI
from urllib import *
from lxml import html
import requests

APP_ID = "1254942267860327"
API_KEY = "b41369a7ec1e753a7274e752afc8b9a4"
ACCESS_TOKEN = "EAACEdEose0cBAO7lNHE7lTQYKKTCIs27ZBZA1a52EJ4WrWOO9Vq7eG9eChnQAXS5EVdGtb35BZAGkQ65Ta9O7qrYQMTEs65VHo9wBAPXz4ZBhQlAXMdiOG4MbxLfGSFe5g2039tXC9AReMAbUkiGtZAZAe7TZBZB0PzvbBZA0AzFHEgZDZD"
graph = GraphAPI(ACCESS_TOKEN)

videos = graph.get(path = 'v2.8/FallonTonight/videos')["data"]
video_ids = []
for video in videos:
	video_ids.append(video["id"])

print(video_ids)
for each_id in video_ids:
	url = "https://www.facebook.com/FallonTonight/videos/"+each_id+"/"
	page = html.fromstring(request.urlopen(url).read())
	print(page.xpath("//span")[0].text)
	el = page.xpath("//span[@class='fcg']")


# Figured out a way to find the best VERIFIED way to get the facebook pages and thus, their 
# corresponding details
DEVELOPER_KEY = "AIzaSyBxuVNgsVOm3GVeIsyrYK1KvyKyWFXY2q8"
CSE_KEY = urllib.parse.quote("010574959533657678901:wcpwn5hwe-k")
url = "https://www.googleapis.com/customsearch/v1?q=fallon&cx="+CSE_KEY+"&key="+DEVELOPER_KEY
requests.get(url)