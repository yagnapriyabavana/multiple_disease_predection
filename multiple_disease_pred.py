# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 16:20:59 2026

@author: chakradhar
"""

import numpy as np
import pickle
import streamlit as st
from streamlit_option_menu  import option_menu

#loading all the saved models
diabetic_model=pickle.load(open(r"C:\Users\chakradhar\Downloads\multi-disease-predection-system\saved_models\trained_model_diabetic.sav",'rb'))
heartdisease_model=pickle.load(open(r"C:\Users\chakradhar\Downloads\multi-disease-predection-system\saved_models\trained_model _heartdisease.sav",'rb'))

#sidebar for navigation
with st.sidebar:
    selected=option_menu('Multiple Disease Predection System',
                        ['Diabetic Predection',
                         'Heart Disease Predection'],  
                        icons=['activity','heart'],
                        default_index=0)
#for diabetic predection
if(selected=='Diabetic Predection'):
    st.title('Diabetic Predection Using Ml')
    #page in the form of columns  
    #getting input from the user
    col1,col2,col3=st.columns(3)
    with col1:
        Pregnancies = st.number_input('Number of Pregnancies', min_value=0)
    with col2:
        Glucose = st.number_input('Glucose Value', min_value=0.0)
    with col3:
        BloodPressure = st.number_input('Blood Pressure Value', min_value=0.0)
    with col1:
        SkinThickness = st.number_input('Skin Thickness Value', min_value=0.0)
    with col2:
         Insulin = st.number_input('Insulin Value', min_value=0.0)
    with col3:
        BMI = st.number_input('BMI Value', min_value=0.0)
    with col1:
        DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function', min_value=0.0)
    with col2:
        Age = st.number_input('Age', min_value=0)
    diab_diagnosis=''
    #creating button for predection
    if st.button('Diabetes Test Result'):
        diab_prediction=diabetic_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
        if (diab_prediction[0]==1):
            diab_diagnosis='The person is Diabetic'
        else:
            diab_diagnosis='The perosn is not Diabetic'
    st.success(diab_diagnosis)


#for heart disease:
    
if(selected == 'Heart Disease Predection'):
    st.title('Heart Disease Predection Using Ml')
    #horizontal input and input features
    col1,col2,col3=st.columns(3)
    with col1:
        age = st.number_input('Age', min_value=0)
    with col2:
        sex = st.number_input('Sex', min_value=0)
    with col3:
        cp = st.number_input('CP Value', min_value=0)
    with col1:
        trestbps=st.number_input('trestbps  Value', min_value=0)
    with col2:
        chol=st.number_input('Chol Value', min_value=0)
    with col3:
        fbs=st.number_input('FB Value', min_value=0)
    with col1:
        restecg=st.number_input('restecg Value', min_value=0)
    with col2:
        thalach=st.number_input('thalach Value', min_value=0)
    with col3:
        exang=st.number_input('exang Value', min_value=0)
        
    with col1:
        oldpeak=st.number_input('oldpeak Value', min_value=0)
    with col2:
        slope=st.number_input('slope Value', min_value=0)
    with col3:
        ca=st.number_input('CA Value', min_value=0)
    with col1:
        thal=st.number_input('Thal Value', min_value=0)
        
    heart_diagnosis=''
    #creating button for predection
    if st.button('Heart Disease Test Result'):
        heart_prediction=heartdisease_model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
        if (heart_prediction[0]==1):
            heart_diagnosis='The person is having a heartdisease'
        else:
            heart_diagnosis='The person is not having a heartdisease'
    st.success(heart_diagnosis)
    