from jikanpy import jikan
import json
import time

jikan = jikan.Jikan()
username_ = 'skr47ch'

# profile ## replace certain keys as they differ in user profile and animlist.
anime_profile = json.loads(json.dumps(jikan.user(username=username_, request='profile')['anime_stats']).replace('on_hold', 'onhold').replace('plan_to_watch', 'plantowatch'))

# anime lists
watching, completed, onhold, dropped, plantowatch = [], [], [], [], []

for item, name in zip([watching, completed, onhold, dropped, plantowatch]
        , ['watching', 'completed', 'onhold', 'dropped', 'plantowatch']):
    page_num = 1
    while len(item) < anime_profile[name]:
        item.extend(jikan.user(username=username_, request='animelist', argument=name, page=page_num)['anime'])
        page_num += 1





# testing
# print(anime_profile['days_watched'], anime_profile['watching'], anime_profile['completed'])