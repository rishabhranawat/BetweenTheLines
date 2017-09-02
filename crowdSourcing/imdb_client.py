import requests
from bs4 import BeautifulSoup


class imbd:
	def __init__(self):
		self.base_url="http://www.imdb.com"

	def get_movie_rating(self, movie_name):
		url = self.base_url+"/find?ref_=nv_sr_fn&q="
		print(url)
		url += movie_name.replace(" ", "+")+"&s=all"
		print(url)
		search_soup = BeautifulSoup(requests.get(url).content, 'html.parser')
		list_table = search_soup.find('table')

		movie = None
		for tr in list_table.find_all('tr'):
			t = tr.find('a')
			movie = t.get('href')
			break
		return self.get_movie_page(self.base_url+movie)

	def get_movie_page(self, movie_page_url):
		print(movie_page_url)
		movie_soup = BeautifulSoup(requests.get(movie_page_url).content, 'html.parser')
		print(movie_soup)
		return float(movie_soup.find("span", {"itemprop":"ratingValue"}).getText())

im = imbd()
print(im.get_movie_rating("start wars"))

