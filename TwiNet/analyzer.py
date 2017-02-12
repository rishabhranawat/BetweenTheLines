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

translator = Translator('8a050fdaf6b74b22af7589f7261a3f0a')

country = "Colombia"
for tweets in d[country][1]:
	all_eng = True
	count = 0
	eng_count = 0
	for each in tweets:
		print(country, count, eng_count)
		if(translator.detect_lang(each) != 'en'):
			count += 1
			if(count > 5):
				all_eng = False
				break
		else:
			eng_count += 1
		if(eng_count > 5):
			break
	if(not all_eng): 
		print(country, len(tweets))
		tweets = translate_tweets(translator, tweets)
	d[country][1] = tweets

	with open("all_translated_tweets.json", "w") as f:
		json.dump(d, f)
	f.close()

with open("all_translated_tweets.json", "w") as f:
	json.dump(d, f)
f.close()