from bottle import Bottle, route, run
from bottle import request, response
from bottle import post, get, put, delete
from pymongo import MongoClient
from json import dumps, loads
from datetime import datetime
from requests.exceptions import HTTPError
import time
from bson import json_util
import athenahealthapi
import datetime
import StringIO
from script.alchemy_analysis import nl_processing
import random

client = MongoClient()
db = client.test

#"ATHENA_TOKEN":"Bearer 2bsm398qq7827s9r85xg8nd5"

key = 'gt5p97xrp5qzur3wecvzn3py'
secret = 'XgptQJgP8jWSdey'
#key = 'rpees3hagjarypdvwdnhjm4f'
#secret = 'BR46MSP5bRreWEA'
version = 'preview1'
practiceid = '195900'

api = athenahealthapi.APIConnection(version, key, secret, practiceid)

app = Bottle()

@app.hook('after_request')
def enable_cors():
    """
    You need to add some headers to each request.
    Don't use the wildcard '*' for Access-Control-Allow-Origin in production.
    """
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'PUT, GET, POST, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'


@app.route('/hello')
def hello():
    return "Hello World!"

@app.route('/ping')
def ping():
    ping = api.GET('/ping')
    return ping

@app.route('/getpatient')
def patient_get():
    patient_id = {'patientid': '29332', 'firstname': 'Nithya' }
    new_patient = api.GET('/patients', patient_id)
    return new_patient

@app.route('/postpatient')
def patient_post():
    patient_info = {
	'lastname': 'Foo',
	'firstname': 'Jason',
	'address1': '123 Any Street',
	'city': 'Cambridge',
	'countrycode3166': 'US',
	'departmentid': 1,
	'dob': '6/18/1987',
	'language6392code': 'declined',
	'maritalstatus': 'S',
	'race': 'declined',
	'sex': 'M',
	'ssn': '123411234',
	'zip': '02139',
    }
    
    new_patient = api.POST('/patients', patient_info)	 
    print new_patient 
    new_patient_id = new_patient[0]['patientid']
    print 'New patient id:'
    print new_patient_id
    return None

@app.route('/getpatients')
def manypatients():
    patient_id = {'departmentid': '1', 'primarydepartmentid': '1','primaryproviderid': '79','veteran': 'Y' }
    new_patient = api.GET('/patients', patient_id)
    return new_patient

@app.route('/analysistext', method='POST')
def analysiss():    
    #value = request.json
    value = request.body.read()
    print value
    v = loads(value)
 #   result1 = nl_processing(v["text"])
    result1 = {
  "emotion": {
    "document": {
      "emotion": {
        "anger": 0.052645,
        "joy": 0.349187,
        "sadness": 0.14315,
        "fear": 0.258821,
        "disgust": 0.049918
      }
    }
  },
  "sentiment": {
    "document": {
      "score": 0.0,
      "label": "neutral"
    }
  },
  "language": "en",
  "entities": [],
  "concepts": [],
  "keywords": [
    {
      "relevance": 0.903313,
      "text": "sun"
    },
    {
      "relevance": 0.871856,
      "text": "west"
    }
  ]
}
    number = random.randint(1,5)
    millis = int(round(time.time() * 1000))
    db.alerts.insert({"patient_id": v["patient_id"], "text": v["text"], "date" : millis , "scores": result1, "risk": {"name": number,"description":"low Risk"} })
    something = db.alerts.find({}).sort("date",-1).limit(1)
    for doc in something:
        print doc
    	return json_util.dumps(doc)

@app.route('/analysisvoice')
def analysis2():

    results = db.alerts.find({"patient_id":"29379"})
    data = []
    for doc in results:
        created = doc["date"]
        text = doc["text"]
        json = {"created": created, "content": text}
        data.append(json)

    for doc in data:
        print doc

    something = personaility_analysis(data)
    print something

    return something

run(app, host='158.85.149.138', port=8080, debug=True)
