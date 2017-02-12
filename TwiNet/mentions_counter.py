import sys
import json

# Helper functions
def get_mentions_structure(nat):
	mentions = {}
	for country, details in nat.items():
		mentions[country] = {}
		for c1, details in nat.items():
			if c1 != country: mentions[country][c1] = 0

	return mentions

with open("aliases.json") as g:
	aliases = json.load(g)
g.close()

with open("all_translated_tweets.json") as h:
	nat = json.load(h)
h.close()

mentions = get_mentions_structure(nat)

for country, details in nat.items():
	x = details[1]
	for e_t in x:
		e_t = e_t.lower()
		let = e_t.split(" ")
		for c1, al in aliases.items():
			for v in al:
				if(country != c1 and v.strip() in let):
					print(v, let)
					mentions[country][c1] += 1

with open("mention_data.json", "w") as f:
	d = json.dump(mentions, f)
f.close()