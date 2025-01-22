import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

st.title('🤖Demand Forecasting of Bicycle Rentals')

st.info('This app builds a machine learning model!')

with st.expander('Data'):
  st.write('**Raw data**')
  df = pd.read_csv('https://raw.githubusercontent.com/lloydong/lo-machinelearning/refs/heads/master/data/bikeshare.csv')
  df
  
  st.write('**X**')
  X_raw = df.drop('count', axis=1)
  X_raw

  st.write('**y**')
  y = df['count']
  y

with st.expander('Data visualization'):
  st.scatter_chart(data=df, x='temperature',y='count', x_label='Temperature,°C', y_label='Total Rentals')

#Data preparations
with st.sidebar:
  st.header('Input features')
  temperature = st.slider('Temperature,°C', 0.82, 41.0, 20.0)
  humidity = st.slider('Humidity, %',0,100,50)
  hour = st.slider('Hour',0,24,19)
  season = st.selectbox('Season', ('1','2','3','4'))
  st.markdown('_Details on Season Variable:_')
  "1 = winter, 2 = spring, 3 = summer, 4 = fall"
  weather = st.selectbox('Weather', ('1','2','3','4'))
  st.markdown('_Details on Weather Variable:_')
  "1: Clear, Few clouds, Partly cloudy, Partly cloudy"
  "2: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist"
  "3: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds"
  "4: Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog"
  
  #Create a DataFrame for the input features
  data = {'temp': temperature,
        'season': season,
        'weather': weather,
        'humidity': humidity,
          'hour': hour
      }
  input_df=pd.DataFrame(data, index=[0])
  # input_rentals = pd.concat([input_df,X_raw],axis=0)

with st.expander('Input features'):
  st.write('**Inputs from Users**')
  input_df

with st.expander('Data preparation'):
  st.write('**Selected features to train the model**')
  feature_cols = ['temperature', 'season', 'weather', 'humidity','hour']
  X = X_raw[feature_cols]
  X

# Model training and inference
## Train the ML model

linreg = LinearRegression()
linreg.fit(X, y)

# Apply model to make prediction
prediction = linreg.predict(input_df)
total_rentals = int(prediction) 

st.subheader('Predicted Total Rentals')
if total_rentals < 0:
  st.success(f"Unfortunately we do not have any bike rentals today!")

#storey_dummies = pd.get_dummies(train_df.storey_range, prefix='storey_range',drop_first=True)
else:
  st.success(f"We have a count of {total_rentals} bike rentals today!")



