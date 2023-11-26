import numpy as np
import joblib
import data
import dataset_creation

loaded_model = joblib.load('heart_rate_classifier.joblib')
f = data.fire()
f.set_user(0,"HealthData")
while True:
    new_heart_rates = np.array([dataset_creation.collect_heart()])
    # Predict the categories for the new heart rates using the loaded model
    predicted_categories = loaded_model.predict(new_heart_rates)
    categories = ["Relaxed","Warm Up","Fat Burning","Aerobic","Anaerobic"]
    f = data.fire()
    f.set_user(0,"HealthData")
    f.write(field="class_HR",predicted_value=categories[predicted_categories[0]])