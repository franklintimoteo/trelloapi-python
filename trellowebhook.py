from dotenv import load_dotenv
from flask import Flask, Response, request
load_dotenv()


app = Flask(__name__)


@app.route('/webhook', methods=['HEAD', 'POST', 'GET'])
def webhook():
    print(request.data)
    print('Tipo de requisição recebida: ', request.method)
    return Response(status=200)


