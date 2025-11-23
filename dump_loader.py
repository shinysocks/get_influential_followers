from os import system
import json

dump = 'followers_1.json'
output = 'followers.txt'
users = []

with open(dump, 'r', encoding='utf-8') as f:
    dump = json.load(f)

for item in dump:
    users.append(item['string_list_data'][0]['value'])
f.close()

with open(output, "w") as file:
    for item in users:
        file.write(item + "\n")
file.close()