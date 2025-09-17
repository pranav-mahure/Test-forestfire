import pickle
from flask import Flask,request,jsonify,render_template,redirect
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

application = Flask(__name__)
app = application

# Import models
ridge_model = pickle.load(open('models/ridge.pkl','rb')) 
scaler_model = pickle.load(open('models/scaler.pkl','rb')) 

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method == 'POST':
        Temperature = float(request.form.get('Temperature'))
        RH = float(request.form.get('RH'))
        Ws = float(request.form.get('Ws'))
        Rain = float(request.form.get('Rain'))
        FFMC = float(request.form.get('FFMC'))
        DMC = float(request.form.get('DMC'))
        ISI = float(request.form.get('ISI'))
        Classes = float(request.form.get('Classes'))
        Region = float(request.form.get('Region'))

        new_scaled_data = scaler_model.transform([[Temperature,RH,Ws,Rain,FFMC,DMC,ISI,Classes,Region]])
        result = ridge_model.predict(new_scaled_data)
        return render_template('home.html',results=result[0]) # Results will be in form of list
    else:
        return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")