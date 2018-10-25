from flask import Flask, jsonify
from flask_cors import CORS
from flask import request

app = Flask(__name__)
CORS(app)


moods = ["fantastic", "good", "ok", 'meh', 'bad']

yearMoods = {
	# 'Jan1': {'mood': 'fantastic', 'note': 'love'},
	# 'Jan2': {'mood': 'bad', 'note':'ds'}
}

@app.route('/')
def index():
    return 'INDEX'

@app.route('/get_mood', methods=['GET'])
def get_mood():
	global yearMoods
	return jsonify(yearMoods)

@app.route('/store_mood', methods=['POST'])
def store_mood():
	global yearMoods
 	yearMoods[request.form.get('squareID')] = {'mood':request.form.get('mood'), 'note':request.form.get('note')}
	return ""


if __name__ == '__main__':
    app.run(debug = True)
