import pandas as pd
import urllib.request, json

from requests.models import requote_uri 


for i in [10]:
    with urllib.request.urlopen(f"https://draft.premierleague.com/api/league/{i}/details") as url:
        data = json.loads(url.read().decode())
        print(data)


import requests

for id_n in range(20):
    print('\nid', id_n)
    if id_n%100==0:
        print(id_n)
    r = requests.get(f"https://draft.premierleague.com/api/league/{id_n}/details")
    r = dict(r.json())
    # if this league id exists
    if 'detail' not in r:
        print(r['league']['min_entries'])
        if r['league']['min_entries'] == 10:
            # get entry ids of the league members
            entry_ids = [i['id'] for i in r['league_entries']]
            print(entry_ids)
            # my own team id: 314319
            if 24773 in entry_ids:
                print('Found it!!', r['league']['id'])