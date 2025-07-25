from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load('model/calories_model.pkl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    name = request.form['name']
    gender = 1 if request.form['gender'] == 'Male' else 0
    age = float(request.form['age'])
    height = float(request.form['height'])
    weight = float(request.form['weight'])
    duration = float(request.form['duration'])
    heart_rate = float(request.form['heart_rate'])
    body_temp = float(request.form['body_temp'])

    data = np.array([[gender, age, height, weight, duration, heart_rate, body_temp]])
    prediction = model.predict(data)[0]

    return render_template('result.html', name=name, prediction=round(prediction, 2))

if __name__ == '__main__':
    app.run(debug=True)
