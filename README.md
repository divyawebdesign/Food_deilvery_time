# 🚚 Food Delivery Time Prediction

A machine learning web application that predicts the estimated time required for food delivery based on delivery details such as delivery person age, rating, distance, order type, and vehicle type.

---

## 📌 Project Overview

Food delivery platforms depend on accurate time estimation to improve customer experience.
This project uses machine learning to predict the **expected delivery time in minutes** using a real dataset.

Users can enter delivery information through a simple web interface, and the trained model predicts the delivery time instantly.

---

## 🎯 Features

* Predict food delivery time using machine learning
* User-friendly web interface
* Real-world delivery dataset
* Fast prediction using a trained model
* Built using Flask for easy deployment

---

## 📂 Dataset

Dataset includes delivery information such as:

* Delivery person age
* Delivery person rating
* Restaurant location
* Delivery location
* Type of order
* Type of vehicle
* Actual delivery time

Source: Kaggle Food Delivery Dataset

---

## 🧠 Machine Learning Model

The model was trained using **Random Forest Regression**.

Steps involved:

1. Data preprocessing
2. Feature selection
3. Model training
4. Model saving using Pickle

---

## 🛠️ Tech Stack

**Programming Language**

* Python

**Libraries**

* Pandas
* Scikit-learn
* NumPy
* Flask

**Frontend**

* HTML
* CSS

---

## 📁 Project Structure

```
food-delivery-time-prediction
│
├── deliverytime.csv
├── train_model.py
├── app.py
│
├── model
│   └── model.pkl
│
└── templates
    ├── index.html
    └── result.html
```

---

## ⚙️ Installation

1. Clone the repository

```
git clone https://github.com/yourusername/food-delivery-time-prediction.git
```

2. Navigate to the project folder

```
cd food-delivery-time-prediction
```

3. Install dependencies

```
pip install pandas scikit-learn flask numpy
```

---

## ▶️ Run the Project

Train the model:

```
python train_model.py
```

Run the web application:

```
python app.py
```

Open the browser and go to:

```
http://127.0.0.1:5000
```

---

## 📊 Example Input

Age: 30
Rating: 4.5
Distance: 5 km
Order Type: Snack
Vehicle: Motorcycle

### Output

Estimated Delivery Time: **28 minutes**

---

## 🔮 Future Improvements

* Integrate real-time traffic data
* Add map-based distance calculation
* Improve prediction accuracy with advanced models
* Deploy the application online
