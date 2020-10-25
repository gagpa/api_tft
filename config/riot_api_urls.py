import os
from string import Template

API_KEY = os.getenv("API_KEY")
link_user_info = Template(f'https://ru.api.riotgames.com/tft/summoner/v1/summoners/by-name/$nickname?api_key={API_KEY}')
link_matches_id = Template(f'https://europe.api.riotgames.com/tft/match/v1/matches/by-puuid/$puuid/ids?count=$count'
                           f'&api_key={API_KEY}')
link_match_info = Template(f'https://europe.api.riotgames.com/tft/match/v1/matches/$match_id?api_key={API_KEY}')

links_template = \
    {
        'user_info': link_user_info,
        'matches_id': link_matches_id,
        'match_info': link_match_info,
    }
