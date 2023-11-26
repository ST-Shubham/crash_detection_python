import numpy as np
import pandas as pd
import dataset_creation
import data
from tensorflow.keras.models import load_model
f = data.fire()
f.set_user(0,"HealthData")
while True:
    updated_dataset = dataset_creation.collect_heart_se()
    updated_dataset = np.array(updated_dataset)
    sequence_length = 10  # Same as used during training
    h_sequences = [updated_dataset[0:10, 0]]
    h = np.array(h_sequences)
    h_model = load_model('heart.h5')

    h_predictions = h_model.predict(h)
    mse_h = np.mean(np.square(h - h_predictions),axis=1)
    threshold_h = [400.08776751] #15.961413079328786

    anomalies = np.array(mse_h > threshold_h)

    if True in anomalies:
        f.write("anom_HR",1)
    else:
        f.write("anom_HR", 0)

