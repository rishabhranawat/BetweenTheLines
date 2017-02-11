import json
from mstranslator import Translator

with open("all_translated_tweets.json") as f:
	d = json.load(f)
f.close()

def translate_tweets(translator, tweets):
	r_tweets = []
	for tweet in tweets:
		r_tweets.append(
			translator.translate(tweet, lang_to='en')
		)
	return r_tweets

translator = Translator('6ff827c947694c21a641a579955c2610')

for country, details in d.items():
	tweets = details[1]
	all_eng = True
	count = 0
	for each in tweets:
		if(translator.detect_lang(each) != 'en'):
			count += 1
			if(count > 1):
				all_eng = False
				break
	print(len(tweets))
	if(not all_eng): 
		print(country)
		tweets = translate_tweets(translator, tweets)
	d[country][1] = tweets

	with open("all_translated_tweets.json", "w") as f:
		json.dump(d, f)
	f.close()

with open("all_translated_tweets.json", "w") as f:
	json.dump(d, f)
f.close()