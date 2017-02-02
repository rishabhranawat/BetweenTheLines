import csv
import json

states = {}

with open("states_lat_long.json") as f:
	lat_long = json.load(f)

for each in lat_long:
	states[each["state"]] = [0, each["latitude"], each["longitude"]]

with open("resist.json") as f:
	resist = json.load(f)

with open("uber.json") as f:
	uber = json.load(f)
	
with open("starbucks.json") as f:
	starbucks = json.load(f)
	
with open("fake_tears.json") as f:
	fake_tears = json.load(f)

with open("all_data.csv", "w") as f:
	writer = csv.writer(f)
	writer.writerow(["State", "#resist", "#deleteuber", "#boycottstarbucks", "#faketears"])
	for key, value in states.items():
		try:
			r = resist[key]
		except:
			r = 0
		try:
			u = uber[key]
		except:
			u = 0
		try:
			s = starbucks[key]
		except:
			s = 0
		try:
			f = fake_tears[key]
		except:
			f = 0
		writer.writerow([key, r, u, s, f])