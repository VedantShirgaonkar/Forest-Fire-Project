from flask  import Flask,request, jsonify, render_template
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

application = Flask(__name__)
app = application

# Importing both pickle files
rf_model = pickle.load(open('models/rf_model.pkl','rb'))
scaler = pickle.load(open('models/scaler.pkl','rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        pass
    else:
        return render_template('home.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5001, debug=True)
