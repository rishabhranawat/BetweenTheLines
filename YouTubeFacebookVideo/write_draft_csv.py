import sys
import csv
import json

with open("draft2.json") as fp:
	data = json.load(fp)

with open("draft2.csv", "w") as f:
	writer = csv.writer(f)

	for key, value in data.items():
		for title, views in value.items():
			writer.writerow([key, title, views["google"], views["fb"]])