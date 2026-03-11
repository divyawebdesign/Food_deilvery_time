import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor

data = pd.read_csv("deliverytime.csv")

# remove spaces
data['Type_of_order'] = data['Type_of_order'].str.strip()
data['Type_of_vehicle'] = data['Type_of_vehicle'].str.strip()

# distance calculation
def distance(lat1,lon1,lat2,lon2):
    return np.sqrt((lat1-lat2)**2 + (lon1-lon2)**2)

data['distance'] = distance(
    data['Restaurant_latitude'],
    data['Restaurant_longitude'],
    data['Delivery_location_latitude'],
    data['Delivery_location_longitude']
)

# encode categorical columns
le_order = LabelEncoder()
le_vehicle = LabelEncoder()

data['Type_of_order'] = le_order.fit_transform(data['Type_of_order'])
data['Type_of_vehicle'] = le_vehicle.fit_transform(data['Type_of_vehicle'])

X = data[['Delivery_person_Age','Delivery_person_Ratings','distance','Type_of_order','Type_of_vehicle']]
y = data['Time_taken(min)']

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)

model = RandomForestRegressor()
model.fit(X_train,y_train)

pickle.dump(model,open("model/model.pkl","wb"))

print("Model trained successfully")