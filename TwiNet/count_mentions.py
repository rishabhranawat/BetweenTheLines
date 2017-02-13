import json

with open("mention_data.json") as f:
	d = json.load(f)
f.close()

vals = {}
for key, value in d.items():
	vals[key] = 0

for key, value in d.items():
	for k, v in value.items():
		vals[k] += v

with open("counter.json", "w") as g:
	d = json.dump(vals, g, indent=4)
g.close()