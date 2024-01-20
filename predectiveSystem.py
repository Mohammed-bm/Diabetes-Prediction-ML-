# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pickle

#load saved model
loaded = pickle.load(open('C:/Users/Mohammed/OneDrive/Desktop/diabetes file/trainedmodel.sav', 'rb'))

input_data = (6, 148, 72, 35, 0, 33.6, 0.627, 50)

#convert the given tuple into array
input_asarray = np.asarray(input_data)

#convert array into 3d
twod_array = input_asarray.reshape(1, -1)

prediction = loaded.predict(twod_array)
print(prediction)

if(prediction[0]==0):
    print('X is not diabetic')

else:
    print('X is diabetic')