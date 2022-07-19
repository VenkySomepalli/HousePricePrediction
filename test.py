# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 07:35:32 2022

@author: venki
"""
import pickle
import streamlit as st
import pandas as pd
# loading the trained model
#df = pd.read_csv("/home/venky/Desktop/Datascience_360/Real_Project_costprediction/VS-Edtech_CourseCost_Model-Deployment/data.csv")
pickle_in = open("C:\\Users\\venki\\OneDrive\\Desktop\\Datascience360\\HousePricePrediction-master\\final_model.pkl", 'rb') 
model = pickle.load(pickle_in)
 
@st.cache()
  
# defining the function which will make the prediction using the data which the user inputs 
def prediction(CRIM, ZN, INDUS, CHAS, NOX, RM, AGE, DIS, RAD, TAX, PTRATIO, B, LSTAT):
   
    # Making predictions 
    prediction = model.predict(pd.DataFrame([[CRIM, ZN, INDUS, CHAS, NOX, RM, AGE, DIS, RAD, TAX,PTRATIO, B,LSTAT]]))
    return prediction
      
  
# this is the main function in which we define our webpage  
def main():       
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:blue;padding:13px"> 
    <h1 style ="color:black;text-align:center;"> Price Prediction of Houses </h1> 
    </div> 
    """
      
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 
      
    # following lines create boxes in which user can enter data required to make prediction 
   
    CRIM = st.sidebar.slider('Crime Rate', 0.006, 90.0)

    #Subject_Name
    ZN  = st.sidebar.slider("Zone:", 0.0, 100.0)

    #Location
    INDUS = st.sidebar.slider("Industries", 0.40, 30.0)

    ## Trainer
    CHAS = st.sidebar.slider("Charles River", 0.0, 1.0)
    NOX = st.sidebar.slider('Nitrix oxide conc.:', 0.30, 0.90 )
    ## Classes
    RM = st.sidebar.slider('Rooms:', 2, 9 )
    AGE = st.sidebar.slider('AGE:', 2, 100 )

    # Hours
    DIS = st.sidebar.slider('Distance:',  )
    # placements
    RAD = st.sidebar.slider('Highways:', 1, 13 )
    TAX = st.sidebar.slider('Tax:', 180, 750  )
    PTRATIO = st.sidebar.slider('Teacher Ratio:', 12, 22  )
    B = st.sidebar.slider('African-American:', 0, 400 )
    LSTAT = st.sidebar.slider('Lower Statues:', 1, 40 )
    
    result =""
    
    # Converting Features into DataFrame

    #features_df  = pd.DataFrame([prediction])
    # when 'Predict' is clicked, make the prediction and store it 
    if st.button('Price'):
       result = prediction(CRIM, ZN, INDUS, CHAS, NOX, RM, AGE, DIS, RAD, TAX, PTRATIO, B, LSTAT)
       
       st.success(f'The Predicted Price of the House is {result[0]:.0f} USD(millions)')
    
     
if __name__=='__main__': 
    main()