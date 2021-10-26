import pickle
import numpy as np
import pandas as pd

model = pickle.load(open('model.pkl', 'rb'))
sex_encod = pickle.load(open('sex_lbl.pkl', 'rb'))
class_names = ['No Pancreatic Disease','Benign Pancreatic Disease','Pancreatic Disease']

def predict(df):
    df = df[['age', 'sex', 'plasma_CA19_9', 'creatinine', 'LYVE1', 'REG1B', 'TFF1','REG1A']]
    df.sex = sex_encod.transform(df.sex)
    numpy_array = df.to_numpy()
    predictions = model.predict(numpy_array)
    output = [class_names[class_predicted] for class_predicted in predictions]
    return output

