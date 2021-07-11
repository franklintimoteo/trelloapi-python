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
  "Recebe dados via json pellso metodo post e repassa para api"
  if request.method in "POST":
    trelobj = process_update_api(request.data, method=request.method)
 
  return Response(status=200)


