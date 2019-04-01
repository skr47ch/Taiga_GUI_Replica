from jikanpy import jikan

jikan = jikan.Jikan()

watching = jikan.user(username='skr47ch', request='animelist', argument='watching')['anime']
completed = jikan.user(username='skr47ch', request='animelist', argument='completed')['anime']

print(len(watching))
