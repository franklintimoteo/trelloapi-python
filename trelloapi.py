import requests
import os
from dotenv import load_dotenv

load_dotenv()


BASE_URL = "https://api.trello.com/1/"
BOARD_TALEON_ID = "6dRtcfQ0" # Board: https://trello.com/b/6dRtcfQ0/python-course

# ID BOARD: 5a173779a28c28e7eb7cb014
final_url = os.path.join(BASE_URL, 'boards', BOARD_TALEON_ID)
params_request = {
    'key': os.environ['TRELLO_API_KEY'],
    'token': os.environ['TRELLO_TOKEN']
}

#r = requests.get(final_url, params=params_request)
headers = {
  'Content-Type': 'application/json'
}
data = {
    'description': 'Meuwebhook.com',
    'callbackURL': 'https://spiffyinsidiousoutcomes.franklindev.repl.co/webhook',
    'idModel': '5a173779a28c28e7eb7cb014'
    }
url = "https://api.trello.com/1/tokens/{token}/webhooks/?key={key}".format(token=os.environ['TRELLO_TOKEN'], key=os.environ['TRELLO_API_KEY'])
response = requests.post(url, params=data)
print("Status code do post", response.status_code)


