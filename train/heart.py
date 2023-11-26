import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense,RepeatVector
from tensorflow.keras.callbacks import ModelCheckpoint
import os
cwd = os.getcwd()

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
        model.fit(X, X, epochs=100, batch_size=32, verbose=2)
        h_predictions = model.predict(X)
        mse_h = np.mean(np.square(X - h_predictions), axis=(0,1))
        print(mse_h)
        return model
model = None
# Load your datasets for each sensor
d = pd.read_csv(os.path.join(cwd, 'data\\heart_rate.csv'))
features = d.iloc[:,0]
features = np.reshape(features,(-1,1))
model = train_lstm_model(features,model,True)

#model.save("heart.h5")
