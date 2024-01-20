# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 21:47:43 2024

@author: Mohammed
"""

import numpy as np
import pickle
import streamlit as st
import sklearn


#load saved model
loaded = pickle.load(open(r"C:\Users\Mohammed\OneDrive\Desktop\diabetes file\trainedmodel.sav", 'rb'))


#creating a function

def diabetes_prediction(input_data):
    
    
    #convert the given tuple into array
    input_asarray = np.asarray(input_data)

    #convert array into 3d
    twod_array = input_asarray.reshape(1, -1)

    prediction = loaded.predict(twod_array)
    print(prediction)

    if(prediction[0]==0):
        return 'X is not diabetic'
    else:
        return 'X is diabetic'
    
def main():
    
    
    st.title('Diabetes Prediction')
    
        
    Pregnancies = st.text_input('Number of Pregnancies')
    Glucose = st.text_input('Glucose Level')
    BloodPressure = st.text_input('Blood Pressure value')
    SkinThickness = st.text_input('Skin Thickness value')
    Insulin = st.text_input('Insulin Level')
    BMI = st.text_input('BMI value')
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    Age = st.text_input('Age of the Person')
    
    
    diagnosis = ''
    
    
    if st.button('Diabetes Test Result'):
        diagnosis = diabetes_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])
        
    
    st.success(diagnosis)
    
    
if __name__ == '__main__':
    main()