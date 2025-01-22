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
  temperature = st.slider('Temperature,°C', 0.82, 41.0, 20.0)
  humidity = st.slider('Humidity, %',0,100,50)
  season = st.selectbox('Season', ('1','2','3','4'))
  "1 = winter, 2 = spring, 3 = summer, 4 = fall"
  weather = st.selectbox('Weather', ('1','2','3','4'))
  "1: Clear, Few clouds, Partly cloudy, Partly cloudy"
  "2: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist"
  "3: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds"
  "4: Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog"

#Create a DataFrame for the input features
  data = {'temp': temperature,
        'humidity': humidity,
        'season': season,
        'weather': weather
      }
  input_df=pd.DataFrame(data, index=[0])
  input_rentals = pd.concat([input_df,X],axis=0)

with st.expander('Input features'):
  st.write('**Input rental**')
  input_df
  st.write('**Combined rentals data**')
  input_rentals





