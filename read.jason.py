import json

with open("test.json",'r') as fr:
	data = json.load(fr)

print(data)
