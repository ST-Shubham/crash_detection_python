import random
import numpy as np
from sklearn.model_selection import train_test_split
import joblib
from sklearn.tree import DecisionTreeClassifier
# Function to categorize heart rate
def categorize_heart_rate(heart_rate):
    max_heart_rate = 220
    percentage = (heart_rate / max_heart_rate) * 100

    if 60 <= percentage < 70:
        return 0#"Relaxed"
    elif 70 <= percentage < 80:
        return 1#"Warm Up"
    elif 80 <= percentage < 90:
        return 2#"Fat Burning"
    elif 90 <= percentage < 100:
        return 3#"Aerobic"
    else:
        return 4#"Anaerobic"

random_heart_rates = [random.randint(60, 220) for _ in range(1000)]
random_heart_rates = np.reshape(random_heart_rates,(-1,1))

heart_rate_categories = [categorize_heart_rate(rate) for rate in random_heart_rates]
d = DecisionTreeClassifier()
d.fit(random_heart_rates,heart_rate_categories)
joblib.dump(d, 'heart_rate_classifier.joblib')
