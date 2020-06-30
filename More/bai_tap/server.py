

from sklearn.externals import joblib
import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
from datetime import datetime
from scipy import signal
from flask_cors import CORS
from flask import render_template

app = Flask(__name__)
CORS(app, support_credentials=True)

# loading my model
model = joblib.load(open("modelKNN.pkl", "rb"))
pca = joblib.load(open("Pca.pkl", "rb"))
sc = joblib.load(open("Scaler.pkl", "rb"))
decode = joblib.load(open("labelEncoder.pkl", "rb"))
# defining a route for only post requests


@app.route('/predict', methods=['POST'])
def predict():
    json_ = request.json
    number = np.array(json_['data'])
    number = number.reshape(1, -1)
    number = signal.savgol_filter(
        number, window_length=17, polyorder=2, deriv=2)
    number = sc.transform(number)
    number = pca.transform(number)
    y_pred = model.predict(number)
    a = str(decode.inverse_transform(y_pred))
    return jsonify({"sucess": "true", "results": a, "time": str(datetime.now())}), 200
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
