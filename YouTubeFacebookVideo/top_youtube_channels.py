from urllib.request import Request, urlopen
from lxml import html

url = "http://vidstatsx.com/youtube-top-100-most-subscribed-channels"
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
page = html.fromstring(urlopen(req).read())
el = page.xpath("//a[@class='user']")
for each in el:
	if(each.text[0] != "#"):
		print(each.text, each.attrib['href'])