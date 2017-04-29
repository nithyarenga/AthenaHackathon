from bottle import route, run
from bottle import request, response
from bottle import post, get, put, delete
from pymongo import MongoClient
from json import dumps, loads
from datetime import datetime
from requests.exceptions import HTTPError

import datetime
import StringIO

client = MongoClient()
db = client.lighthouse

@get('/hello')
def hello():
    return "Hello World!"

run(host='158.85.149.138', port=8080, debug=True)
