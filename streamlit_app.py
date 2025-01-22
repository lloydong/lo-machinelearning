import streamlit as st
import pandas as pd

st.title('🤖Machine Learning App')

st.info('This app builds a machine learning model!')

with st.expander('Data'):
  st.write('**Raw data**')
  df = pd.read_csv('https://raw.githubusercontent.com/lloydong/lo-machinelearning/refs/heads/master/data/bikeshare.csv')
  df

  st.write('**X**')
  X = df.drop('count', axis=1)
  X

  st.write('**y**')
  y = df.count
  y

with st.expander('Data visualization'):
  st.scatter_chart(data=df, x='temp',y='count', x_label='Temperature,°C', y_label='Total Rentals')

#Data preparations
with st.sidebar:
  st.header('Input features')
  "","temperature", "season", "humidity"
  temperature = st.slider('Temperature,°C', 0.82, 41.0, 20.0)
  season = st.selectbox('Season', ('1','2','3','4'))
  humidity = st.slider('Humidity, %',0,100,50)





