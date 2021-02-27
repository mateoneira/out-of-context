from flask import Flask, jsonify
import json
import os
import numpy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

with open('messages.json') as _file:
    messages = json.load(_file)

def select_random():
    return numpy.random.choice(messages)

@app.route("/")
def start():
    response = jsonify(select_random())
    return response

    

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host = '0.0.0.0', port=port)
    # app.run()

