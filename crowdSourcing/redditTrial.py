import praw
from sklearn.feature_extraction.text import CountVectorizer


reddit = praw.Reddit(client_id='eR6bB9c2Juu6mQ',
                     client_secret='uW4z9EaCIfFbbexRBS1WpGsHB2s',
                     user_agent='my user agent')

URL = "https://www.reddit.com/r/movies/comments/4i35uf/\
official_discussion_captain_america_civil_war/?st=j4w491jj&sh=22ea1167"

submission = reddit.submission(url=URL)
top_level_comments = []
for top_level_comment in submission.comments:
	try: 
		for comment in top_level_comment.replies:
			top_level_comments.append(comment.body)
	except: pass

cv = CountVectorizer()
cv_fit=cv.fit_transform(top_level_comments)

print(cv.get_feature_names())
print(cv_fit.toarray())