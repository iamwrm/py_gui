import json

with open('sched_data.txt', 'r') as infile:
    data = json.load(infile)
print(data)