import json

with open("list.json") as f:
	d = json.load(f)
f.close()

batch_1 = {}
batch_2 = {}
batch_3 = {}
batch_4 = {}
batch_5 = {}

count = 0
n = 1
batch = batch_1
for country, screen_name in d.items():
	if(count != 0 and count % 10 == 0):
		n+=1
		batch = globals()['batch_'+str(n)]
	batch[country] = screen_name
	count += 1

for i in range(0, 5, 1):
	batch_name = 'batch_'+str(i+1)
	batch = globals()[batch_name]
	with open(batch_name+".json", "w") as f:
		json.dump(batch, f)
	f.close()
