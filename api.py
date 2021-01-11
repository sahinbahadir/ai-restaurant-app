from flask import request, jsonify, Response
from flask_cors import CORS, cross_origin
import flask
import get_recommendations
import collaborative_v2
import json

app = flask.Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['DEBUG'] = True
FILENAME = 'en_son.csv'

@app.route('/popularity', methods=['GET'])
def popularity():
    day = int(request.args.get('day')) - 1
    hour = request.args.get('hour')
    hour = hour[:2] + ':00' + '-' + str(int(hour) + 1) + ':00'
    val = get_recommendations.popularityBased(FILENAME, day, hour)
    values = [val[cat] for cat in val.keys()]
    return jsonify([item for sublist in values for item in sublist])

@app.route('/collaborative', methods=['GET'])
def collaborative():
    if not request.args:
        return '<h1>Parametre Girmelisiniz!</h1>'
    
    foodNames = request.args.get('foodNames').split(',')
    retVal = collaborative_v2.getMostPreferredList(FILENAME, foodNames)
    if retVal == -1:
        return Response("{\"success\":false, \"msg\": \"No recommendation found.\"}", status=404, mimetype='application/json')

    values = [retVal[cat] for cat in retVal.keys()]
    return jsonify([item for sublist in values for item in sublist])

@app.route('/foods', methods=['GET'])
@cross_origin()
def getAllFoods():
    data = dict()
    with open('db.json', 'r') as f:
        data = json.load(f)
        f.close()
    return jsonify(data['foods'])

@app.route('/categories', methods=['GET'])
@cross_origin()
def getAllCategories():
    data = dict()
    with open('db.json', 'r') as f:
        data = json.load(f)
        f.close()
    return jsonify(data['categories'])

app.run()
