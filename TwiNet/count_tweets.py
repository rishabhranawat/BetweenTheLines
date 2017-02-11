import json

total = 0
all_tweets = {}
for i in range(0, 5, 1):
	batch = "batch_"+str(i+1)+"_tweets.json"
	with open(batch) as f:
		d = json.load(f)
	for country, details  in d.items():
		total += len(details[1])
		all_tweets[country] = details
print(total, len(all_tweets))

with open("all_batches_tweets.json", "w") as f:
	json.dump(all_tweets, f)
f.close()

