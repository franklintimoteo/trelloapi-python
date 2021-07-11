import logging
import json
from json.decoder import JSONDecodeError
from collections import namedtuple

from .types import Model, Action

logging.basicConfig()
logger = logging.getLogger('trelloapi')
logger.setLevel('DEBUG')

def process_update_api(data, method):
  TrelloObject = namedtuple('TrelloObject', ('model', 'action'))

  try:
    data = serialize_to_dict(data)
  except (JSONDecodeError, TypeError) as error:
    raise Exception('Invalid type to decoder new update', error)
  
  model = Model.deserialize_json(data)
  action = Action.deserialize_json(data)

  logger.debug("Loaded new update: %s Action:%s" %(model, action.type))
  
  return TrelloObject(model, action)  

def serialize_to_dict(data: dict):
  return json.loads(data)
 