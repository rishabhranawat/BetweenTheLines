import praw

reddit = praw.Reddit(client_id='eR6bB9c2Juu6mQ',
                     client_secret='uW4z9EaCIfFbbexRBS1WpGsHB2s',
                     user_agent='my user agent')

# for submission in reddit.subreddit('learnpython').hot(limit=10):
#     print(submission.title)

URL = 'https://www.reddit.com/r/AskReddit/comments/688ik4/teachers_of_reddit_what_is_wrong_with_modern/?st=j4csvnr9&sh=ba977b59'
submission = reddit.submission(url=URL)

for top_level_comment in submission.comments:
	try: 
		for comment in top_level_comment.replies:
			print(comment.body)
	except: pass