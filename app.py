import os
from flask import Flask, jsonify, request
import json
from routes import register_routes

app = Flask(__name__)

register_routes(app)

if __name__ == '__main__':
    port = os.environ.get('PORT',5000)
app.run(debug=False, host='0.0.0.0',port=port)
