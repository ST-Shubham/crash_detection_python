# Import necessary libraries
import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model

route = ["First route","Second route","Third route"]
lap = ["First lap","Second lap","Third lap"]
model = None
threshold = 0
# Load your datasets for each sensor
for i in range(len(route)):
    for j in range(len(lap)):
        print(i+1,j+1)
        d = pd.read_csv('data/{}/{}/BS_Route{}_gyroscope_{}.csv'.format(route[i],lap[j],i+1,j+1))
        features = d.iloc[:,2:5]
        # Create sequences for the LSTM model
        sequence_length = 10  # Adjust as needed
        sequences = []
        for k in range(len(features) - sequence_length):
            sequence = features[k:k+sequence_length]
            sequences.append(sequence)
        sequences = np.array(sequences)
        loaded_model = load_model("gyroscope.h5")
        predicted_values = loaded_model.predict(sequences)
        # Calculate the mean squared error (MSE) as a measure of reconstruction error
        mse = np.mean(np.square(sequences - predicted_values),axis=(0,1))
        # Define a threshold for anomaly detection (e.g., using percentiles)
        threshold += mse  # Adjust the percentile as needed
print(threshold/9)

threshold = 0
# Load your datasets for each sensor
for i in range(len(route)):
    for j in range(len(lap)):
        print(i+1,j+1)
        d = pd.read_csv('data/{}/{}/BS_Route{}_accelerometer_{}.csv'.format(route[i],lap[j],i+1,j+1))
        features = d.iloc[:,2:5]
        # Create sequences for the LSTM model
        sequence_length = 10  # Adjust as needed
        sequences = []
        for k in range(len(features) - sequence_length):
            sequence = features[k:k+sequence_length]
            sequences.append(sequence)
        sequences = np.array(sequences)
        loaded_model = load_model("accelerometer.h5")
        predicted_values = loaded_model.predict(sequences)
        # Calculate the mean squared error (MSE) as a measure of reconstruction error
        mse = np.mean(np.square(sequences - predicted_values),axis=(0,1))
        # Define a threshold for anomaly detection (e.g., using percentiles)
        threshold += mse  # Adjust the percentile as needed
print(threshold/9)

threshold = 0
# Load your datasets for each sensor
for i in range(len(route)):
    for j in range(len(lap)):
        print(i+1,j+1)
        d = pd.read_csv('data/{}/{}/BS_Route{}_magnetometer_{}.csv'.format(route[i],lap[j],i+1,j+1))
        features = d.iloc[:,2:5]
        # Create sequences for the LSTM model
        sequence_length = 10  # Adjust as needed
        sequences = []
        for k in range(len(features) - sequence_length):
            sequence = features[k:k+sequence_length]
            sequences.append(sequence)
        sequences = np.array(sequences)
        loaded_model = load_model("magnetometer.h5")
        predicted_values = loaded_model.predict(sequences)
        # Calculate the mean squared error (MSE) as a measure of reconstruction error
        mse = np.mean(np.square(sequences - predicted_values),axis=(0,1))
        # Define a threshold for anomaly detection (e.g., using percentiles)
        threshold += mse  # Adjust the percentile as needed
print(threshold/9)