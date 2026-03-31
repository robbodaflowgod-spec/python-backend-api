from flask import Flask, jsonify
from flask_cors import CORS  # NEW: Import CORS
import datetime

app = Flask(__name__)
CORS(app)  # NEW: This allows any website to request data from this API

@app.route('/')
def home():
    return {
        "message": "The Backend is Live and CORS-enabled!",
        "status": "Success"
    }

@app.route('/api/time')
def get_time():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    return jsonify({
        "server_time": current_time, 
        "timezone": "UTC",
        "status": "Online"
    })

# NEW: A mock data route (simulating a database)
@app.route('/api/status')
def get_status():
    return jsonify({
        "project": "Subscription Recovery Tool",
        "version": "1.0.0",
        "database_connected": False  # We will change this to True later
    })

if __name__ == '__main__':
    app.run()