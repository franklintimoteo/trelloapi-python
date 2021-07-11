import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()


BASE_URL = "https://api.trello.com/1/webhooks/"

headers = {
   "Accept": "application/json"
}

data_webhook = {
  'key': os.environ.get('TRELLO_API_KEY'),
  'token': os.environ.get('TRELLO_TOKEN'),
  'callbackURL': "https://trelloapi.bardevnull.repl.co/webhook",
  'idModel': 'not defined',
}

data = {
  'key': os.environ.get('TRELLO_API_KEY'),
  'token': os.environ.get('TRELLO_TOKEN'),
}
print(data)
def get_model_id():
  board_id = "6dRtcfQ0"
  _url = f"https://api.trello.com/1/boards/{board_id}"
  idModelBoard = requests.get(_url, params=data)
  return idModelBoard.json()['id']

def set_webhook(): 
  idModel = get_model_id()
  data_webhook['idModel'] = idModel
  response = requests.post(BASE_URL, headers=headers, params=data_webhook)
  
  return response

if __name__ == "__main__":
  response = set_webhook()
  print(response.content)
  

