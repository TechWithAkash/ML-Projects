
# // app.py
import pickle
from flask import Flask, request, jsonify,render_template
import pandas as pd
import numpy as np

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

application = Flask(__name__)

app = application

# Route for the Home Page
@app.route("/")
def home():
    return render_template('index.html')

# Route for the Prediction
@app.route('/predict', methods=['GET','POST'])
def predictdata():
    if request.method == 'GET':
        return render_template('home.html')
    else:                                           
        data = CustomData(
            gender = request.form.get('gender'),
            race_ethnicity= request.form.get('race_ethnicity'),
            parental_level_of_education = request.form.get('parental_level_of_education'),
            lunch = request.form.get('lunch'),
            test_preparation_course = request.form.get('test_preparation_course'),
            reading_score = float(request.form.get('reading_score')),
            writing_score = float(request.form.get('writing_score'))

        )

        pred_df = data.get_data_as_data_frame()
        print(pred_df)

        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(pred_df)
        print(results)

        return render_template('home.html', results=results[0])
    




if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)

