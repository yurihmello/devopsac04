import os
from flask import Flask, jsonify, request
from math import sqrt


app = Flask(__name__)

@app.route('/')

def fibonacci():
    prox = 1
    ant = 0
    x = 0
    resp = "0,"
    while x <=50:

        y = prox
        prox = prox + ant
        ant = y
        x += 1
        resp += str(prox) + ","
    
    return resp

if __name__ == "__main__":
    
    port = int(os.environ.get("PORT", 5000))
    
    app.run(host='0.0.0.0', port=port)
