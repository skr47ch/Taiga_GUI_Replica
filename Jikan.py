from jikanpy import jikan
import time

jikan = jikan.Jikan()
username_ = 'skr47ch'

# profile
anime_profile = jikan.user(username=username_, request='profile')['anime_stats']

# anime lists
watching = []
completed  = []
onhold = []
dropped = []
plantowatch = []

print(anime_profile)

for item, name in zip([watching, completed, dropped]
        , ['watching', 'completed', 'dropped']):
    page_num = 1
    while len(item) < anime_profile[name]:
        item.extend(jikan.user(username=username_, request='animelist', argument=name, page=page_num)['anime'])
        page_num += 1





# testing
# print(anime_profile['days_watched'], anime_profile['watching'], anime_profile['completed'])