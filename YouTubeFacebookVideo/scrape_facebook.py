from facepy import GraphAPI
from urllib import request
from lxml import html

APP_ID = "1254942267860327"
API_KEY = "b41369a7ec1e753a7274e752afc8b9a4"
ACCESS_TOKEN = "EAACEdEose0cBAL3q9chllvbD3b0fCfiPxEDnktAJbvSNGg431rrXNoU03p9F2m7gyehgXlg2EkT1TRZCnpqSxobM9F9ISG8SPZCn1sfOskZAvx89x3jZA8RrLlZA7jhtIEVPZAU8qc15tvEIvgAG2Mep7SbIIuZACsdiZAkPQHbizwZDZD"
graph = GraphAPI(ACCESS_TOKEN)

videos = graph.get(path = 'v2.8/FallonTonight/videos')["data"]
video_ids = []
for video in videos:
	video_ids.append(video["id"])

for each_id in video_ids:
	url = "https://www.facebook.com/FallonTonight/videos/"+each_id+"/"
	page = html.fromstring(request.urlopen(url).read())

	el = page.xpath("//span[@class='fcg']")
	print("Video ID: "+each_id+" "+el[0].text)