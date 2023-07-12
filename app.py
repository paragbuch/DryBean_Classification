import pickle
from flask import Flask, request, app, jsonify, url_for, render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
# model = pickle.load(open('Bean_model.pickle', 'rb'))
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST','GET'])
def predict():
    if request.method == 'POST':
        try:
            Area=int(request.form['Area'])
            MajorAxisLength=float(request.form['MajorAxisLength'])
            MinorAxisLength=float(request.form['MinorAxisLength'])
            Eccentricity=float(request.form['Eccentricity'])
            Extent=float(request.form['Extent'])
            Solidity=float(request.form['Solidity'])
            roundness=float(request.form['roundness'])
            ShapeFactor2=float(request.form['ShapeFactor2'])
            ShapeFactor4=float(request.form['ShapeFactor4'])
            filename = 'Bean_model.pickle'
            loaded_model = pickle.load(open(filename, 'rb')) # loading the model file from the storage
            # predictions using the loaded model file
            prediction=loaded_model.predict([[Area,MajorAxisLength, MinorAxisLength, Eccentricity, Extent, Solidity, roundness,ShapeFactor2,ShapeFactor4]])
            print('prediction is', prediction)
            # showing the prediction results in a UI
            return render_template('home.html',prediction=prediction)

        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'
    # return render_template('results.html')
    else:
        return render_template('index.html')
if __name__ == "__main__":
    app.run(debug=True)