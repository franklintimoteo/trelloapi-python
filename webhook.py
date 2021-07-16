from dotenv import load_dotenv
from flask import Flask, Response, request
from trelloapi.trelloapi import process_update_api
import logging

logger = logging.getLogger('trelloapi.webhook')
logging.getLogger('werkzeug').setLevel('ERROR')
load_dotenv()

app = Flask(__name__)

@app.route('/webhook', methods=['HEAD', 'POST', 'GET'])
def webhook():
  "Recebe dados via json pelo metodo post e repassa para api"
  if request.method in "POST":
    trellobj = process_update_api(request.data, method=request.method)

    dispatch(trellobj)

  return Response(status=200)


tags = {
  'green': '🟩',
  'yellow': '🟨',
  'orange': '🟧', 
  'red': '🟥',
  'purple': '🟪',
  'blue': '🟦',
  'sky': '🟦',
  'lime': '🟩',
  'pink': '🟪',
  'black': '⬛',
}
def dispatch(trellobj):
  actionType = trellobj.action.type
  selected_func = functions_process_action[actionType]

  if selected_func:
    selected_func(trellobj)

def process_addLabelToCard(trellobj):
  msg = "{board} adicinou {color}{nameTag} a {card}"
  board = trellobj.action.data['board'].name
  tag = trellobj.action.data['label'].name
  color = trellobj.action.data['label'].color
  card = trellobj.action.data['card'].name
  print(
    msg.format(board=board, color=tags[color], nameTag=tag,card=card)
  )

functions_process_action = {
  'addLabelToCard': process_addLabelToCard,
  'updateCheckItemStateOnCard': False,
  'updateCheckItemStateOnCard': False,
  'removeLabelFromCard': False,
  'updateCard': False,  # Move card from list to list trello
}
