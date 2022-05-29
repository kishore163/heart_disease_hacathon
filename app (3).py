import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np
import pandas as pd
import joblib

model=joblib.load('heart_disease_prediction')

with st.sidebar:
  selected=option_menu(
      menu_title='Main_Menu',
      options=['Home','Upload your Info']
  )
if selected=='Home':
  st.title('Heart Disease Predictor')
  st.subheader("This is an app which predicts whether you are prone to heart diseae or not")
  st.image(r"/content/drive/MyDrive/hackathon/heart_homepage.webp",width=600)

if selected=='Upload your Info':
  flag=0
  st.title("YOU CAN UPLOAD THE information related to you heart to check about its health")
  st.image(r"/content/drive/MyDrive/hackathon/heart_upload page.jpg")
  arr=[]
  st.write('Press enter in your keyboard after entering each value')
  age=st.number_input("Age",min_value=0,max_value=100)
  arr.append(age)
  sex=st.selectbox('Sex',['Male','Female'])
  if sex=='Male':
      arr.append(1)
  else:
      arr.append(0)
  cp=st.number_input('chest_pain type')
  arr.append(cp)
  res_bp=st.number_input('resting blood pressure')
  arr.append(res_bp)
  chol=st.number_input('cholestrol level')
  arr.append(chol)
  fast_bp=st.selectbox('fasting blood sugar',['present','not present'])
  if fast_bp=='present':
      arr.append(1)
  else:
      arr.append(0)
  restecg=st.number_input('resting electrocardiographic result')
  arr.append(restecg)
  max_hr=st.number_input('maximum heart rate achieved')
  arr.append(max_hr)
  exc_ag=st.selectbox('excercise induced anguina',['yes','no'])
  if exc_ag=='yes':
      arr.append(1)
  else:
      arr.append(0)
  st_dep=st.number_input('ST depression')
  arr.append(st_dep)
  slope=st.number_input('Slope of ST depression',min_value=0,max_value=2)
  arr.append(slope)
  ca=st.slider('number of major vessels',min_value=0,max_value=4)
  arr.append(ca)
  thal=st.slider('thal',min_value=0,max_value=3)
  arr.append(thal)
  flag=1
  check=st.selectbox('did you upload the data correctly?',['no','yes'])

  if len(arr)==13 and check =='yes' :
    values=np.array(arr).reshape(1,-1)
    pred=model.predict(values)
    if pred[0]==0:
        st.header('Congrats!! your heart is perfectly fine')
    else:
        st.header('your heart seems to be having a problem! please go to a verified doctor asap!!')