from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


moods = ["fantastic", "good", "ok", 'meh', 'bad']

@app.route('/')
def index():
    return 'INDEX'

@app.route('/get_mood', methods=['GET'])
def get_mood():
	return jsonify({
        "mood": moods[0],
        "squareID": "Jan1",
        "note": "",
    })

if __name__ == '__main__':
    app.run(debug = True)
