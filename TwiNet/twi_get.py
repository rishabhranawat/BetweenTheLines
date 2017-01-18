import tweepy

auth = tweepy.OAuthHandler("7ORmqhp1lXxpazSzpTGVVNAv6", "KXwjMsUcf0cKLIZ94D76GYwJeAhQ2qbUlxp2OnENVDQXIAz3Nh")
auth.set_access_token("3530340917-urj3UuRWL6frj2FtdhQjj6v0PpVF0PoJy6hp6og", "eW9ZyEZID417pFtZDTLwUI95u60TCcict290qxnBIXleE")

api = tweepy.API(auth)
user = api.get_user('realDonaldTrump')


public_tweets = user.home_timeline()
for tweet in public_tweets:
    print(tweet.text)