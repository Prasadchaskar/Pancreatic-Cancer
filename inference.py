import pickle
import numpy as np
import pandas as pd

model = pickle.load(open('Cancer/model.pkl', 'rb'))
sex_encod = pickle.load(open('Cancer/sex_lbl.pkl', 'rb'))
class_names = ['Benign Pancreatic Disease','No Pancreatic Disease','Pancreatic Disease']

def predict(df):
    df = df[['age', 'sex', 'plasma_CA19_9', 'creatinine', 'LYVE1', 'REG1B', 'TFF1','REG1A']]
    df.sex = sex_encod.transform(df.sex)
    numpy_array = df.to_numpy()
    predictions = model.predict(numpy_array)
    output = [class_names[class_predicted] for class_predicted in predictions]
    return output

age = 68
sex = 'M'
plasma_CA19_9 = 654.002944
creatinine = 0.52026
lyve1 =7.058209
reg = 156.241000
tff = 525.178000
rega = 735.281222



df = pd.DataFrame({ 
    'age':[age],
    'sex':[sex], 
    'plasma_CA19_9':[plasma_CA19_9], 
    'creatinine':[creatinine], 
    'LYVE1':[lyve1],
    'REG1B':[reg],
    'TFF1':[tff], 
    'REG1A':[rega]

})
print(predict(df))