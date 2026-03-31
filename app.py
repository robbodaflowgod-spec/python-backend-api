from flask import Flask, jsonify
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return "The Backend is Running!"

@app.route('/api/time')
def get_time():
    # This logic happens on the server, not the browser
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    return jsonify({"server_time": current_time, "status": "Online"})

if __name__ == '__main__':
    app.run()