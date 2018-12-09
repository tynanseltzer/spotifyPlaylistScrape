import spotipy
from scrapeUtil import authenticate
from datetime import datetime
import csv

# Instance setup, authenticate with me
token = authenticate('1229234382')
sp = spotipy.Spotify(auth=token)
# File write
f = open("results.csv", 'w')
writer = csv.writer(f)

# How I go through different names
code = 124815456
# Num people
counter = 0
# Generating different people, by search around code
k = 0
NUM_PEOPLE = 500

while counter < NUM_PEOPLE:
    print(counter)
    code += (-1 ** k) * k

    person = str(code)
    # See if real person
    try:
        name = sp.user(person)['display_name']
        print(name)
    except spotipy.client.SpotifyException:
        k += 1
        continue

    l = sp.user_playlists(user=person, limit=50)
    if len(l) > 0:
        counter += 1
        # Go through each playlist
    for i in range(len(l['items'])):
        single = []
        single.append(name)
        query = sp.user_playlist(user=person, playlist_id=l['items'][i]['id'])
        single.append(query['name'])
        if query['owner']['id'] != person:
            continue
        dates = []
        # Find playlist creation date
        for j in range(len(query['tracks']['items'])):
            single.append(query['tracks']['items'][j]['track']['name'])

            date = datetime.strptime(query['tracks']['items'][j]['added_at'][:10],
                                     '%Y-%m-%d')
            dates.append(date)

        # Write out
        if len(query['tracks']['items']) > 0:
            single.insert(2, str(min(dates))[:10])
            writer.writerow(single)


    k += 1
