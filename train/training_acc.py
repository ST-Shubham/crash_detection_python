import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense,RepeatVector
from tensorflow.keras.callbacks import ModelCheckpoint

# Define function for creating and training LSTM model
def train_lstm_model(data,model,flag):
    sequence_length = 10  # Modify based on your choice
    sequences = [data[i - sequence_length:i, :] for i in range(sequence_length, len(data))]
    X = np.array(sequences)
    if flag:
        model = Sequential()
        model.add(LSTM(units=128, activation='relu', input_shape=(X.shape[1], X.shape[2]),return_sequences=False))
        model.add(RepeatVector(X.shape[1]))
        model.add(LSTM(128, return_sequences=False))
        model.add(Dense(units=X.shape[2]))  # Adjust units based on your data dimensions
        model.compile(optimizer='adam', loss='mse')
        model.summary()
    model.fit(X, X, epochs=10, batch_size=32, verbose=2)
    return model

route = ["First route","Second route","Third route"]
lap = ["First lap","Second lap","Third lap"]
model = None
# Load your datasets for each sensor
for i in range(len(route)):
    for j in range(len(lap)):
        print(i+1,j+1)
        d = pd.read_csv('data/{}/{}/BS_Route{}_accelerometer_{}.csv'.format(route[i],lap[j],i+1,j+1))
        features = d.iloc[:,2:5]
        scaler = StandardScaler()
        features = scaler.fit_transform(features)
        flag = False
        if i==0 and j==0:
            flag=True
        model = train_lstm_model(features,model,flag)

#model.save("accelerometer.h5")

