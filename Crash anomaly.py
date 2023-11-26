import numpy as np
import pandas as pd
import dataset_creation
import data
from tensorflow.keras.models import load_model
f = data.fire()
f.set_user(2,"CrashData")
while True:
    updated_dataset = dataset_creation.collect()
    updated_dataset = np.array(updated_dataset)
    sequence_length = 10  # Same as used during training
    acc_sequences = [updated_dataset[0:10, 0:3]]
    acc = np.array(acc_sequences)
    mag_sequences = [updated_dataset[0:10, 3:6]]
    mag = np.array(mag_sequences)
    gyro_sequences = [updated_dataset[0:10, 6:9]]
    gyro = np.array(gyro_sequences)
    acc_model = load_model("accelerometer.h5")
    mag_model = load_model("magnetometer.h5")
    gyro_model = load_model("gyroscope.h5")

    acc_predictions = acc_model.predict(acc)
    #mag_predictions = mag_model.predict(mag)
    gyro_predictions = gyro_model.predict(gyro)

    mse_acc = np.mean(np.square(acc - acc_predictions),axis=1)
    #mse_mag = np.mean(np.square(mag - mag_predictions),axis=1)
    mse_gyro = np.mean(np.square(gyro - gyro_predictions),axis=1)


    #threshold = np.mean(mse) + np.std(mse)
    threshold_acc = [4.08776751,18.68272273,25.113749] #15.961413079328786
    threshold_mag = [32.06421947,43.14468697,66.50664858 ]#47.23851834001067
    threshold_gyro = [0.00703285,0.00219432,0.00179894] #0.0036753712283384746

    anomalies_acc = np.array(mse_acc > threshold_acc)
    #anomalies_mag = np.array(mse_mag > threshold_mag)
    anomalies_gyro = np.array(mse_gyro > threshold_gyro)
    anomalies = np.concatenate((anomalies_gyro,anomalies_acc))

    if True in anomalies:
        f.write("crash_prediction",1)
        print("yes")
    else:
        f.write("crash_prediction", 0)
        print("no")

