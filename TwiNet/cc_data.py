import json
import pickle

with open("mention_data.json") as f:
	d = json.load(f)
f.close()

with open("countries_abb.json") as g:
	c = json.load(g)
g.close()


codes = {}
for each in c:
	codes[each["name"]] = each["code"]

data = {}

for country, details in d.items():
	sub_d = {}
	for c1, v1 in details.items():
		sub_d[codes[c1]] = v1
	data[codes[country]] = sub_d

with open("abb_data.json", "w") as f:
	json.dump(data, f)
f.close()