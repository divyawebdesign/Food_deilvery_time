from flask import Flask,render_template,request
import numpy as np
import pickle

app = Flask(__name__)

model = pickle.load(open("model/model.pkl","rb"))

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict',methods=['POST'])
def predict():

    age = float(request.form['age'])
    rating = float(request.form['rating'])
    distance = float(request.form['distance'])
    order = int(request.form['order'])
    vehicle = int(request.form['vehicle'])

    data = np.array([[age,rating,distance,order,vehicle]])

    prediction = model.predict(data)

    result = round(prediction[0],2)

    return render_template("result.html",prediction=result)

if __name__ == "__main__":
    app.run(debug=True)