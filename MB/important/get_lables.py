import json

final_data = {}
states = {}
labels = {}
with open("stateab.json") as f:
	ab = json.load(f)

with open("resist.json") as f:
	resist = json.load(f)

with open("uber.json") as f:
	uber = json.load(f)
	
with open("starbucks.json") as f:
	starbucks = json.load(f)
	
with open("fake_tears.json") as f:
	fake_tears = json.load(f)

for each in ab:
	state = each["name"]
	abr = each["abbreviation"]

	left = 0
	right = 0
	try:
		r = resist[state]
	except:
		r = 0
	try:
		u = uber[state]
	except:
		u = 0
	try:
		s = starbucks[state]
	except:
		s = 0
	try:
		f = fake_tears[state]
	except:
		f = 0

	left = r + u
	right = s + f
	winner = ""
	electoralVotes = left + right
	if(electoralVotes == 0):
		winner = "UNDECIDED"
	elif(right > left):
		winner = "Republican"
		win_rate = (right/(right+left))*100
		if(win_rate > 50 and win_rate < 60): "Light Republican"
		elif(win_rate > 75): "Heavy Republican"
	elif(right < left):
		winner = "Democrat"
		win_rate = (left/(right+left))*100
		print(win_rate)
		print(left, right)
		if(win_rate > 50 and win_rate < 60): "Light Democrat"
		elif(win_rate > 75): "Heavy Democrat"
	else:
		winner = "UNDECIDED"

	if(electoralVotes == 0):
		states[abr] = {"fillKey": winner, 
			"left": 0,
			"right": 0
		}
		labels[abr] = "Tie"
	else:
		left = round(((u/electoralVotes)*100+(r/electoralVotes)*100), 2)
		right = round(((f/electoralVotes)*100+(s/electoralVotes)*100), 2)
		states[abr] = {
			"fillKey": winner,
			"left": left,
			"right": right
		}
		
		if(left > right):
			labels[abr] = str(left)+"%"
		else:
			labels[abr] = str(right)+"%"

# with open("map_data.json", "w") as f:
# 	json.dump(states, f)

with open("labels.json", "w") as f:
	json.dump(labels, f)
