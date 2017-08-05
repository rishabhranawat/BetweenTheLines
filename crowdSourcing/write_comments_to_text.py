import praw
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA

class WriteComments:

	def __init__(self):
		self.CLIENT_ID = 'eR6bB9c2Juu6mQ'
		self.CLIENT_SECRET = 'uW4z9EaCIfFbbexRBS1WpGsHB2s'
		self.reddit = praw.Reddit(client_id=self.CLIENT_ID,
			client_secret=self.CLIENT_SECRET, user_agent='my user agent')

	def setMovieNameUrl(self, name, url):
		self.movieName = name
		self.URL = url

	def writeComments(self):
		reddit = self.reddit
		print(self.URL)
		submission = reddit.submission(url=self.URL)

		submission.comments.replace_more(limit=0)
		sia = SIA()
		with open('movie_comments/'+self.movieName+'_top_level_comments.txt', 'w') as f:
			for top_level_comment in submission.comments:
				score = (top_level_comment.score)
				sentiment = sia.polarity_scores(top_level_comment.body)['pos']
				replies = len(top_level_comment.replies.list())
				s = str(score)+", "+str(sentiment)+", "+str(replies)
				f.write(s)
				f.write("\n")
			f.close()


movie_links = []
with open('movie_links', 'r') as f:
	lines = f.readlines()
	for each in lines:
		movie_links.append(each.split(", "))

write = WriteComments()
for name_link in movie_links:
	print(name_link)
	write.setMovieNameUrl(name_link[0], name_link[1])
	write.writeComments()
# url = "https://www.reddit.com/r/movies/comments/2ljk71/official_discussion_interstellar_wide_release/"
# write = WriteComments(url, "intersetllar")
# write.writeComments()