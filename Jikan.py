from jikanpy import jikan
import json
import time

jikan = jikan.Jikan()
username_ = 'skr47ch'

# anime lists
# ## replace certain keys as they differ in user profile and animlist.
anime_profile = json.loads(json.dumps(jikan.user(username=username_, request='profile')['anime_stats']).replace('on_hold', 'onhold').replace('plan_to_watch', 'plantowatch'))
watching, completed, onhold, dropped, plantowatch = [], [], [], [], []
for item, name in zip([watching, completed, onhold, dropped, plantowatch]
        , ['watching', 'completed', 'onhold', 'dropped', 'plantowatch']):
    page_num = 1
    try:
        while len(item) < anime_profile[name]:
            item.extend(jikan.user(username=username_, request='animelist', argument=name, page=page_num)['anime'])
            page_num += 1
    except Exception:
        pass


# user statistics
user_stats = json.loads(json.dumps(jikan.user(username=username_)['anime_stats']))

anime_count = user_stats['total_entries']
episode_count = user_stats['episodes_watched']
days_watched = user_stats['days_watched']
mean_score = user_stats['mean_score']
# testing
# print(anime_profile['days_watched'], anime_profile['watching'], anime_profile['completed'])