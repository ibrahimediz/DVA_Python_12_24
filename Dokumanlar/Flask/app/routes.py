from app import app
from flask import jsonify


data = {
    1: {'name': 'John', 'age': 30},
    2: {'name': 'Jane', 'age': 25},
    3: {'name': 'Bob', 'age': 35}
}

@app.route('/')
def index():
    return "<h1>Hello, World!</h1>" #Hello, World!"

@app.route('/api/data',methods=['GET'])
def json():
    veri = data.values()
    return jsonify(veri)