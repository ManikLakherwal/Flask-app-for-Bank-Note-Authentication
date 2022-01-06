# -*- coding: utf-8 -*-
"""
@author: ManikLakherwal 
"""

# -*- coding: utf-8 -*-
"""
@author: ManikLakherwal
"""


import numpy as np
import pickle
import pandas as pd
import streamlit as st 

from PIL import Image



pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)


def welcome():
    return "Welcome All"


def predict_heart_disease(Age,Sex,ChestPainType,RestingBP,Cholesterol,FastingBS,RestingECG,MaxHR,ExerciseAngina,Oldpeak,ST_Slope):
    
    """Let's Predict heart disease 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: Age
        in: query
        type: number
        required: true
      - name: Sex
        in: query
        type: number
        required: true
      - name: ChestPainType
        in: query
        type: number
        required: true
      - name: RestingBP
        in: query
        type: number
        required: true
      - name: Cholesterol
        in: query
        type: number
        required: true
      - name: FastingBS
        in: query
        type: number
        required: true
      - name: RestingECG
        in: query
        type: number
        required: true
      - name: MaxHR
        in: query
        type: number
        required: true
      - name: ExerciseAngina
        in: query
        type: number
        required: true
      - name: Oldpeak
        in: query
        type: number
        required: true
      - name: ST_Slope
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """
   
    prediction=classifier.predict([[Age,Sex,ChestPainType,RestingBP,Cholesterol,FastingBS,RestingECG,MaxHR,ExerciseAngina,Oldpeak,ST_Slope]])
    print(prediction)
    return prediction



def main():
    st.title("Heart Disease")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Heart disease ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    Age = st.text_input("Age","Type Here")
    Sex = st.text_input("Sex 1:Male   2:Female","Type Here")
    ChestPainType= st.text_input("ChestPainType👉🏻Enter 0: Asymptomatic   1: Atypical Angina  2: Non-Anginal Pain  3: Typical Angina]","Type Here")
    RestingBP = st.text_input("Resting blood pressure [mm Hg]","Type Here")
    Cholesterol= st.text_input("Serum cholesterol [mm/dl","Type Here")
    FastingBS= st.text_input("Fasting blood sugar [1: if FastingBS > 120 mg/dl   0: otherwise]","Type Here")
    RestingECG= st.text_input("Resting electrocardiogram results [1: Normal   2: having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV)   0: showing probable or definite left ventricular hypertrophy by Estes' criteria","Type Here")
    MaxHR= st.text_input("Maximum heart rate achieved [Numeric value between 60 and 202]","Type Here")
    ExerciseAngina= st.text_input(" Exercise-induced angina [1: Yes    0: No]","Type Here")
    Oldpeak= st.text_input("Oldpeak: ST [Numeric value measured in depression]","Type Here")
    ST_Slope= st.text_input("ST_Slope: The slope of the peak exercise ST segment [2: upsloping   1: flat  0: downsloping]","Type Here")
    result=""
    if st.button("Predict"):
        result=predict_heart_disease(Age,Sex,ChestPainType,RestingBP,Cholesterol,FastingBS,RestingECG,MaxHR,ExerciseAngina,Oldpeak,ST_Slope)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")

if __name__=='__main__':
  main()
    
