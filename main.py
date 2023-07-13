from flask import Flask, jsonify
from flask_restful import reqparse, abort, Api, Resource
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})
api = Api(app)
@app.route('/')
def hello_world():
    return 'Hello, World!'
@app.route('/sum/<string:n>')
def sum(n):
    result = {
        "one" : n , 
        "ten" : int(n) * 10 
    }
    return jsonify(result)
if __name__ == "__main__":
    app.run(debug=True)