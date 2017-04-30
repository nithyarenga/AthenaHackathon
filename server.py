from bottle import Bottle, route, run
from bottle import request, response
from bottle import post, get, put, delete
from pymongo import MongoClient
from json import dumps, loads
from datetime import datetime
from requests.exceptions import HTTPError
<<<<<<< HEAD
 
import athenahealthapi
import datetime
import StringIO
from script.alchemy_analysis import nl_processing

client = MongoClient()
db = client.test

#"ATHENA_TOKEN":"Bearer 2bsm398qq7827s9r85xg8nd5"

#key = 'gt5p97xrp5qzur3wecvzn3py'
#secret = 'XgptQJgP8jWSdey'
key = 'rpees3hagjarypdvwdnhjm4f'
secret = 'BR46MSP5bRreWEA'
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
#    result1 = nl_processing(v["text"])
    print v["text"]
#    print result1
    result = {
     "emotion": {
       "document": {
         "emotion": {
           "anger": 0.103053,
           "joy": 0.116034,
           "sadness": 0.099817,
           "fear": 0.495298,
           "disgust": 0.187159
         }
       }
     },
     "sentiment": {
       "document": {
         "score": 0.922588,
         "label": "positive"
       }
     },
     "language": "en",
     "entities": [
       {
         "relevance": 0.931351,
         "text": "Bruce Banner",
         "type": "Person",
         "count": 3
       },
       {
         "relevance": 0.288696,
         "text": "Wayne",
         "type": "Person",
         "count": 1
       }
     ],
     "concepts": [
       {
         "relevance": 0.964521,
         "text": "Jeph Loeb",
         "dbpedia_resource": "http://dbpedia.org/resource/Jeph_Loeb"
       },
       {
         "relevance": 0.869445,
         "text": "Stan Lee",
         "dbpedia_resource": "http://dbpedia.org/resource/Stan_Lee"
       },
       {
         "relevance": 0.846319,
         "text": "Jack Kirby",
         "dbpedia_resource": "http://dbpedia.org/resource/Jack_Kirby"
       },
       {
         "relevance": 0.833633,
         "text": "John Byrne",
         "dbpedia_resource": "http://dbpedia.org/resource/John_Byrne"
       },
       {
         "relevance": 0.814538,
         "text": "Marvel Comics",
         "dbpedia_resource": "http://dbpedia.org/resource/Marvel_Comics"
       },
       {
         "relevance": 0.752684,
         "text": "Roger Stern",
         "dbpedia_resource": "http://dbpedia.org/resource/Roger_Stern"
       },
       {
         "relevance": 0.749798,
         "text": "Rick Jones",
         "dbpedia_resource": "http://dbpedia.org/resource/Rick_Jones_(comics)"
       },
       {
         "relevance": 0.74342,
         "text": "Hulk",
         "dbpedia_resource": "http://dbpedia.org/resource/Hulk_(film)"
       }
     ],
     "keywords": [
       {
         "relevance": 0.996186,
         "text": "Bruce Banner"
       },
       {
         "relevance": 0.963163,
         "text": "Bruce Wayne"
       },
       {
         "relevance": 0.637163,
         "text": "Hulk"
       },
       {
         "relevance": 0.612517,
         "text": "Superman"
       },
       {
         "relevance": 0.5912,
         "text": "BATMAN"
       }
     ]
    }   

    return result    

run(app, host='158.85.149.138', port=8080, debug=True)
