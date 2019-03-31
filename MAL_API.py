import requests
import json
from bs4 import BeautifulSoup
import time

time.sleep(3)

url_animelist = 'https://myanimelist.net/animelist/skr47ch/load.json?offset=0&status=7'
user = 'skr47ch'

sourceanimelist = requests.get(url_animelist).text
source_json = json.loads(sourceanimelist)

watching = (x for x in source_json if x['status'] == 1)
completed = (x for x in source_json if x['status'] == 2)

# profile_url = 'https://myanimelist.net/profile/skr47ch'
# response = requests.get(profile_url)
# print(response.text)
#
# soup = BeautifulSoup(response, features='html.parser')
# content = soup.find('div', class_='stats anime')

