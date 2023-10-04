from flask import Flask,jsonify,request
from model import Model


app = Flask(__name__)

@app.route("/")
def greet():
    return "hello! api is up!!"

@app.route("/get-prediction", methods = ['POST'])
def get_sentiment():
    data = request.get_json()
    return jsonify(Model().predictor(data["month"],data["year"],data["type"]))

if __name__ == "__main__":
    app.run()