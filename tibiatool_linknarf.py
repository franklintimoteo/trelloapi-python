import requests
import os
import json
from json import JSONDecodeError

BASE_API_URL = "https://api.tibiadata.com/v2/"


def nrr_cache(request_func):
    "No Repeat Request"
    content = dict() # type: dict
    _last_arg = "" # type: str
    def cached_request(*args, **kargs):
        nonlocal content
        nonlocal _last_arg
        
        _last_arg = args[0]
        if not content or 'error' in content.get('highscores', {}).get('data', {}):
            content = request_func(*args, **kargs)
        elif args[0].lower() != _last_arg:
            content = request_func(*args, **kargs)
        return content
        
    return cached_request

def parse_json(content):
    content_parsed = dict()
    try:
        content_parsed = json.loads(content)
    except JSONDecodeError as error:
        raise Exception('Error on decode json tibia data. ', error)

    return content_parsed

@nrr_cache
def request_highscores(world="Belobra"):
    """Get a list of highscores 

    Args:
        world (string): check on website tibia.com a world
        category (string): experience, magic, shielding, charmpoints, achievements
        vocation (string): druid, knight, paladin or sorcerer.

        Consult: https://tibiadata.com/doc-api-v2/highscores/# 
        more details
    """
   
    if not isinstance(world, str):
        raise TypeError('Invalid schema, try: request_highscores(world)')

    highscore_url = os.path.join(BASE_API_URL, 'highscores', world)+'.json'

    result = requests.get(highscore_url)
    content = parse_json(result.content)
    
    return content


def request_character(name: str):

    name = str(name)
    character_url = os.path.join(BASE_API_URL, 'characters', name)+'.json'
    
    result = requests.get(character_url)
    content = parse_json(result.content)

    return content
