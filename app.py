from flask import Flask,request,render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData,PredictPipeline

application=Flask(__name__)

app=application

## Route for a home page

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('home.html')
    else:
        data=CustomData(
            car_name=request.form.get('car_name'),
            brand=request.form.get('brand'),
            model=request.form.get('model'),
            vehicle_age=request.form.get('vehicle_age'),
            km_driven=request.form.get('km_driven'),
            seller_type=request.form.get('seller_type'),
            fuel_type=request.form.get('fuel_type'),
            transmission_type=request.form.get('transmission_type'),
            mileage=float(request.form.get('mileage')),
            engine=float(request.form.get('engine')),
            max_power=float(request.form.get('max_power')),
            seats=float(request.form.get('seats'))
        )
        pred_df=data.get_data_as_data_frame()
        print(pred_df)
        print("Before Prediction")

        predict_pipeline=PredictPipeline()
        print("Mid Prediction")
        results=predict_pipeline.predict(pred_df)
        print("after Prediction")
        return render_template('home.html',results=results[0])
    

if __name__=="__main__":
    app.run(host="0.0.0.0")        