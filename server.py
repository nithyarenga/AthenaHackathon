from bottle import route, run
from bottle import request, response
from bottle import post, get, put, delete
from pymongo import MongoClient
from json import dumps, loads
from datetime import datetime
from requests.exceptions import HTTPError
 
import athenahealthapi
import datetime
import StringIO

client = MongoClient()
db = client.lighthouse

#"ATHENA_TOKEN":"Bearer 2bsm398qq7827s9r85xg8nd5"

key = 'gt5p97xrp5qzur3wecvzn3py'
secret = 'XgptQJgP8jWSdey'
version = 'preview1'
practiceid = '195900'

api = athenahealthapi.APIConnection(version, key, secret, practiceid)

@get('/hello')
def hello():
    return "Hello World!"

@get('/ping')
def ping():
    ping = api.GET('/ping')
    return ping
@get('/getpatient')
def patient_get():
    patient = api.GET('/patients/29352')
    return patient    

run(host='158.85.149.138', port=8080, debug=True)
