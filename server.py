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
from script.personality_insight import personaility_analysis
import random
import os 
import cPickle as pickle

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

def scoring(personality_res):
   result = personality_res['emotion']['document']['emotion']
   score = 0
   if result['anger'] > 0.8:
       score += 4
   elif result['anger'] > 0.5:
       score += 3
   elif result['anger'] > 0.3:
       score += 2
   if result['sadness'] > 0.8:
       score += 4
   elif result['sadness'] > 0.4:
       score += 3
   elif result['sadness'] > 0.2:
       score += 2
   if result['joy'] > 0.8:
       score += -4
   elif result['joy'] > 0.5:
       score += -3
   elif result['joy'] > 0.3:
       score += -2
   if result['fear'] > 0.8:
       score += 3
   elif result['fear'] > 0.5:
       score += 2
   elif result['fear'] > 0.3:
       score += 1
   if result['disgust'] > 0.8:
       score += 3
   elif result['disgust'] > 0.5:
       score += 2
   elif result['disgust'] > 0.3:
       score += 1
   if score < 1:
       score = 1
   elif score > 5:
       score = 5
   return score


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

@app.route('/test')
def manypatients():
    patient_id = {'departmentid': '1', 'primarydepartmentid': '1','primaryproviderid': '79','veteran': 'Y' }
    new_patient = api.GET('/patients', patient_id)
    return new_patient

@app.route('/getpatients')
def test():
    patient_id = {'departmentid': '1', 'primarydepartmentid': '1','primaryproviderid': '79','veteran': 'Y' }
    final = []
    new_patient = api.GET('/patients', patient_id)
    for i in new_patient["patients"]:
       result = {"patientid":i["patientid"],"firstname":i["firstname"] ,"lastname": i["lastname"],"sex":i["sex"],"veteran":i["veteran"],"zip":i["zip"],"dob":i["dob"]}
       final.append(result)
    print final
    return dumps(final)

@app.route('/analysistext', method='POST')
def analysiss():    
    #value = request.json
    value = request.body.read()
    print value
    v = loads(value)
    TEST_MODE = False
    filename = 'test_alchemy.pickle'
    if os.path.isfile(os.path.join('./', filename)) and TEST_MODE:
       print('Loading Pickle')
       result = pickle.load(open(os.path.join('./', filename)))
    else:
       result = nl_processing(v["text"])
       pickle.dump(result, open(os.path.join('./', filename), 'wb'))
#    result1 = {
#  "emotion": {
#    "document": {
#      "emotion": {
#        "anger": 0.052645,
#        "joy": 0.349187,
#        "sadness": 0.14315,
#        "fear": 0.258821,
#        "disgust": 0.049918
#      }
#    }
#  },
#  "sentiment": {
#    "document": {
#      "score": 0.0,
#      "label": "neutral"
#    }
#  },
#  "language": "en",
#  "entities": [],
#  "concepts": [],
#  "keywords": [
#    {
#      "relevance": 0.903313,
#      "text": "sun"
#    },
#    {
#      "relevance": 0.871856,
#      "text": "west"
#    }
#  ]
#}
    number = random.randint(1,5)
    millis = int(round(time.time() * 1000))
    number = scoring(result)
    des = ""
    if number == 1:
       des = "Low Risk"
    elif number == 2:
       des = "Intermediate Low Risk"
    elif number ==3 :
       des = "Medium Risk"
    elif number == 4:
       des = "Intermediate High Risk"
    else:
       des = "High Risk"
    db.alerts.insert({"patient_id": v["patient_id"], "text": v["text"], "date" : millis , "scores": result, "risk": {"name": number,"description": des} })
    something = db.alerts.find({}).sort("date",-1).limit(1)
    for doc in something:
        print doc
    	return json_util.dumps(doc)

@app.route('/riskfactor', method='POST')
def risk():
   value = request.body.read()
   print value
   v = loads(value)
   something = db.alerts.find({"patient_id": v["patient_id"]}).sort("date",-1).limit(1)
   for doc in something:
       result = {"risk": doc["risk"]["name"], "patient_id": v["patient_id"]}
       return json_util.dumps(result)

@app.route('/riskpatient', method='POST')
def risking():
    value = request.body.read()
    print value
    v = loads(value)
    results = db.alerts.find({"patient_id":v["patient_id"]})
    data = []
    for doc in results:
        created = doc["date"]
        text = doc["risk"]["name"]
        json = {"time": created, "risk": text}
        data.append(json)
    return json_util.dumps(data)

@app.route('/messages')
def risking():
    results = db.alerts.find({"patient_id":"29380"}).sort("date",-1).limit(10)
    data = []
    for doc in results:
        created = doc["date"]
        text = doc["text"]
        json = {"time": created, "text": text}
        data.append(json)
    return json_util.dumps(data)

@app.route('/analysisvoice')
def analysis2():

    #value = request.body.read()
    #v = loads(value)
    #results = db.alerts.find({"patient_id":v["patient_id"]})
    results = db.alerts.find({"patient_id":"29380"})

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

#@app.route('/appointment')
#def appt():
#    patient_id = {'patientid': '29332' }
#    new_patient = api.GET('/patients/:patientid/appointments', patient_id)

@app.route('/getnote', method='POST')
def get_note():

    value = request.body.read()
    print value
    v = loads(value)

    result = api.GET('/patients/' + v["patient_id"] + '/appointments', {"patientid":v["patient_id"], "practiceid":"195900", "limit":"1"})

    print result

    payload = {"appointmentid":result["appointments"][0]["appointmentid"]}
    return api.GET('/appointments/' + result["appointments"][0]["appointmentid"] + '/notes', payload)

@app.route('/postnote', method='POST')
def post_note():

    value = request.body.read()
    print value
    v = loads(value)

    result = api.GET('/patients/' + v["patient_id"] + '/appointments', {"patientid":v["patient_id"], "practiceid":"195900", "limit":"1"})

    print result

    payload = {"appointmentid":result["appointments"][0]["appointmentid"], "notetext":v["notetext"]}
    api.POST('/appointments/' + result["appointments"][0]["appointmentid"] + '/notes', payload)


@app.route('/appointments', method='POST')
def appointments():

    value = request.body.read()
    print value
    v = loads(value)

    return api.GET('/patients/' + v["patient_id"] + '/appointments', {"patientid":v["patient_id"], "practiceid":"195900", "limit":"1"})


run(app,host="0.0.0.0", port=8080, debug=True)
