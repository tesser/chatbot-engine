#!/usr/bin/env python3

from random import randint

from flask import Flask, jsonify, request
from flask_cors import CORS

from forecaster import Forecaster
from geocoder import Geocoder
from query_parser import QueryParser

PORT = 9000
RESPONSES = [
        "Hrm... How about asking me about the weather?",
        "I don't know about that... Want to know about the weather?",
        "I'm not really into that type of thing. Let's talk about the weather.",
        "You must be off your rocker at the moment. Come back when you want to talk weather."
        ]

app = Flask(__name__)
CORS(app)

store = {}
geocoder = Geocoder()

@app.route('/chat/messages', methods=['GET', 'POST'])
def chat_messages():
    if request.form['action'] == 'join':
        store[request.form['user_id']] = { "messages": [ "Hello %s!" % (request.form['name']) ] }
        reply = store[request.form['user_id']]['messages'][-1]

    elif request.form['action'] == 'message':
        location = QueryParser(request.form['text']).location()
        if location:
            lat, lng = geocoder.encode(location)
            reply = Forecaster(lat, lng).weather_summary()
            if not reply:
                reply = "Hrm... couldn't find any weather info for that place."
        else:
            reply = RESPONSES[randint(0, len(RESPONSES) - 1)]

    return jsonify({
        "messages": [
            {
                "type": "text",
                "text": reply
            }
        ]
    })

app.run(port=PORT)
