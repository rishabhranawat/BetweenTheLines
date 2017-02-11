import json

total = 0
for i in range(0, 5, 1):
	batch = "batch_"+str(i+1)+"_tweets.json"
	with open(batch) as f:
		d = json.load(f)
	for country, details  in d.items():
		total += len(details[1])

print(total)