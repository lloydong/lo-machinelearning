import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

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
  st.title("Bike Rentals Analysis")
  sns.lmplot(x='temp', y='total_rentals', data=bikes, scatter_kws={'alpha':0.1})
  st.pyplot(plt)
