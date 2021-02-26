from flask import Flask, jsonify
import json
import numpy

app = Flask(__name__)

with open('messages.json') as _file:
    messages = json.load(_file)

def select_random():
    return numpy.random.choice(messages)

@app.route("/")
def start():
    response = jsonify(select_random())
    return response

    

if __name__ == "__main__":
    app.run()

