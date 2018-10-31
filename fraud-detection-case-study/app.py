from flask import Flask, url_for, request, render_template
import json
import requests
import socket
import time
from datetime import datetime
import parse
from pymongo import MongoClient
import pickle
app = Flask(__name__)
URL = 'http://galvanize-case-study-on-fraud.herokuapp.com/data_point'
# Opening a pointer to our MongoDB
db_client = MongoClient()
db = db_client['fraud_case_study']
table = db['fraud']
# Opening up our pickled model
with open('model.pkl', 'rb') as infile:
    model = pickle.load(infile)
@app.route('/')
def api_root():
    go_to_score_page = '''
            <form action="/score" >
                <input type="submit" value = "Find Out Here."/>
            </form>'''
    return "Let's get ready to RummBULLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL!\nLezz find out if we gots a frauder all up in our Heroku server son! " +go_to_score_page
@app.route('/score', methods=['GET', 'POST'])

def score():
    # DATA.append(json.dumps(request.json, sort_keys=True, indent=4, separators=(',', ': ')))
    # TIMESTAMP.append(time.time())
    new_data, object_id = parse.request(URL,table)
    prediction, proba = parse.predict(new_data, model)
    table.update_many({'object_id':object_id},{'$set':{'prediction':int(prediction), 'fraud_probability' : float(proba)}})
    if proba > 0.7:
        risk = 'high'
    elif proba >= 0.5:
        risk = 'medium'
    else:
        risk = 'low'
    if prediction == 1:
        out = 'We got possible Fraud! Assemble your investigators!'
    else:
        out = 'Nope, no Fraud up in here son.'
    return 'Risk Level : {}\n'.format(risk) + out
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)