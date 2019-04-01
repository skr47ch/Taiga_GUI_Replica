from jikanpy import jikan

jikan = jikan.Jikan()
username_ = 'skr47ch'

# profile
anime_profile = jikan.user(username=username_, request='profile')['anime_stats']

# anime lists
watching = []
completed  = []

page_num=1
while len(watching) < anime_profile['watching']:
    watching.extend(jikan.user(username=username_, request='animelist', argument='watching', page=page_num)['anime'])
    page_num += 1

page_num=1
while len(completed) < anime_profile['completed']:
    completed.extend(jikan.user(username=username_, request='animelist', argument='completed', page=page_num)['anime'])
    page_num += 1

# testing
print(anime_profile['days_watched'], anime_profile['watching'], anime_profile['completed'])