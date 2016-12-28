import sys
import csv
import json

with open("draft.json") as fp:
	data = json.load(fp)

with open("draft.csv", "w") as f:
	writer = csv.writer(f)

	for key, value in data.items():
		for title, views in value.items():
			writer.writerow([key.encode('utf-8'), title.encode('utf-8'), views["google"].encode('utf-8'), views["fb"].encode('utf-8')])