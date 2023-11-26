import numpy as np
import pandas as pd
import data
import time
def collect():
    arr = []
    start_time = time.time()
    f = data.fire()
    for i in range(10):
        # initial_dataset = pd.read_csv("dataset.csv")
        f.set_user(2,"CrashData")
        documents = f.load_documents()
        new_data = [documents[0]['a_x'], documents[0]['a_y'], documents[0]['a_z'], documents[0]['m_x'], documents[0]['m_y'],
                     documents[0]['m_z'], documents[0]['g_x'], documents[0]['g_y'], documents[0]['g_z']]
        arr.append(new_data)
        elapsed_time = time.time() - start_time
        # if elapsed_time >= 1:
        #     return arr
        # Pause for 0.1 seconds
        # time.sleep(0.1)
    return arr
def collect_heart_se():
    arr = []
    start_time = time.time()
    f = data.fire()
    for i in range(10):
        # initial_dataset = pd.read_csv("dataset.csv")
        f.set_user(0,"HealthData")
        documents = f.load_documents()
        new_data = [documents[0]['HeartRate'], documents[0]['Temperature'], documents[0]['Pedometer']]
        arr.append(new_data)
        elapsed_time = time.time() - start_time
        # if elapsed_time >= 1:
        #     return arr
        # Pause for 0.1 seconds
        # time.sleep(0.1)
    return arr
def collect_heart():
    arr = []
    start_time = time.time()
    f = data.fire()
        # initial_dataset = pd.read_csv("dataset.csv")
    f.set_user(0,"HealthData")
    documents = f.load_documents()
    new_data = [documents[0]['HeartRate']]
    elapsed_time = time.time() - start_time
        # if elapsed_time >= 1:
        #     return arr
        # Pause for 0.1 seconds
        # time.sleep(0.1)
    return new_data