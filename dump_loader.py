#   Timothy Faust 2025
#
#   this takes all the json dumps from meta account center
#   and creates a single-column .txt of followers.
#   which can be used by get_influential_followers.py
#   https://accountscenter.instagram.com/info_and_permissions/


from os import system
import glob
import json

file_list = glob.glob('followers*.json')

output = 'followers.txt'
users = []

for file in file_list:
    with open(file, 'r', encoding='utf-8') as f:
        dump = json.load(f)

    for item in dump:
        users.append(item['string_list_data'][0]['value'])
    f.close()

with open(output, "w") as file:
    for item in users:
        file.write(item + "\n")
file.close()
