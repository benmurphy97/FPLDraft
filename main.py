import pandas as pd
import requests 

r = requests.get(f"https://draft.premierleague.com/api/entry/314319/event/1")
r = dict(r.json())

