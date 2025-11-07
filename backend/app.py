from flask import Flask, jsonify
import json
import os
from flask_cors import CORS
import socket


app = Flask(__name__)

CORS(app)
@app.route('/')
def api_health():
    return jsonify({"status": "ok"}), 200
    
@app.route('/hostinfo')
def host_info():
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    return jsonify({'hostname': hostname, 'ip': ip})

@app.route('/api')
def serve_json():
    
    with open(os.path.join(os.path.dirname(__file__), 'data.json'), 'r') as f:
        data = json.load(f)
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
