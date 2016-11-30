# @author - Rishabh Ranawat for BetweenTheLines
# Gets the top youtube channels with their usernames
# Outputs a separate file with the youtube names

from urllib.request import Request, urlopen
from lxml import html
import requests, json


# Source of the top youtube channels - vistatsx.com
url = "http://vidstatsx.com/youtube-top-100-most-subscribed-channels"
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
page = html.fromstring(urlopen(req).read())
el = page.xpath("//a[@class='user']")

vals = {}

for each in el:
	if(each.text[0] != "#"):
		vals[each.text] = each.attrib["href"].replace("/youtube-channel", "")
print(json.dumps(vals, indent=4))

with open('youtube_channels.json', 'w') as fp:
	json.dump(vals, fp)

# for key, val in vals.items():
# 	url = "https://www.googleapis.com/youtube/v3/channels?part=contentDetails&forUsername="+val.replace("/", "")+"&key=AIzaSyBxuVNgsVOm3GVeIsyrYK1KvyKyWFXY2q8"
# 	channel_data = json.loads(requests.get(url).text)
# 	uploads_id = channel_data['items'][0]['contentDetails']['relatedPlaylists']['uploads']
# 	k_url = "https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=10&playlistId="+uploads_id+"&key=AIzaSyBxuVNgsVOm3GVeIsyrYK1KvyKyWFXY2q8"
# 	videos_data = json.loads(requests.get(k_url).text)
# 	items = videos_data['items']
# 	for each in items:
# 		video_id = each['snippet']['resourceId']['videoId']
# 		v_url = "https://www.googleapis.com/youtube/v3/videos?part=statistics&id="+video_id+"&key=AIzaSyBxuVNgsVOm3GVeIsyrYK1KvyKyWFXY2q8"
# 		details = json.loads(requests.get(v_url).text)
# 		print("Title: "+each['snippet']['title'])
# 		print("commentCount "+details['items'][0]['statistics']['commentCount'])
# 		print("likeCount "+details['items'][0]['statistics']['likeCount'])
# 		print("viewCount "+details['items'][0]['statistics']['viewCount'])
# 		print()
