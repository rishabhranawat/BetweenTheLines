import praw
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA

class WriteComments:

	def __init__(self, url, movieName):
		self.CLIENT_ID = 'eR6bB9c2Juu6mQ'
		self.CLIENT_SECRET = 'uW4z9EaCIfFbbexRBS1WpGsHB2s'
		self.URL = url
		self.movieName = movieName
		self.reddit = praw.Reddit(client_id=self.CLIENT_ID,
			client_secret=self.CLIENT_SECRET, user_agent='my user agent')

	def writeComments(self):
		reddit = self.reddit
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

url = "https://www.reddit.com/r/movies/comments/2ljk71/official_discussion_interstellar_wide_release/"
write = WriteComments(url, "intersetllar")
write.writeComments()