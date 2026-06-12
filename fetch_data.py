import pandas as pd
import json
#read data from API 

from nhlpy import NHLClient

client = NHLClient()

season = '20242025'
gameids = client.helpers.game_ids_by_season(season=season)

print(f"Number of games found: {len(gameids)}")
print(type(gameids))

shots = []

for game in gameids[:100]:
    pbp = client.game_center.play_by_play(game_id=game)
    plays = pbp.get('plays', [])
    for play in plays:
        event_type = play.get('typeDescKey')

        if event_type == "shot-on-goal" or event_type == 'goal':
            shots.append(play)

with open('shots.json', 'w') as f:
    json.dump(shots, f)
#print(shots)
#df_hockey = pd.json_normalize(shots)
#drop irrelevant columns

#data.columns
#data = data.drop(columns=['sunrise', 'sunset', 'moonphase', 'description', 'icon', 'stations', 'datetime'])
