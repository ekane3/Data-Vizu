"""
Author : EKANE EMILE
github :  ekane3.github.io
Subject : Streamlit with Lab1 second dataset
"""
import streamlit as st
# Streaming the first dataset
import numpy as np
import pandas as pd 
import time
import plotly.figure_factory as ff
import matplotlib.pyplot as plt


#Title bar
st.sidebar.title("Currently streaming ❤")
st.sidebar.markdown("Select the Charts/Plots according to:")
project_title = st.sidebar.text_input("You can change the title of this project")
if project_title:
    st.title(project_title)
else:
    st.title("New York trip data")

st.markdown("The dashboard will visualize new york trip data")
st.markdown("New York City comprises 5 boroughs sitting where the Hudson River meets the Atlantic Ocean. At its core is Manhattan, a densely populated borough that’s among the world’s major commercial, financial and cultural centers. Its iconic sites include skyscrapers such as the Empire State Building and sprawling Central Park. Broadway theater is staged in neon-lit Times Square.")

#LOAD DATA
#Connecting to endpoint to get csv file 

DATA_URL = ("../data/ny-trips-data.csv")
#@st.cache(persist=True) #( If you have a different use case where the data does not change so very often, you can simply use this)


# Function to load data
@st.cache
def load_data(): 
    data = pd.read_csv(DATA_URL)
    #Convert date/time column type from object to datetime
    data['tpep_pickup_datetime'] = pd.to_datetime(data['tpep_pickup_datetime'])
    data['tpep_dropoff_datetime'] = pd.to_datetime(data['tpep_dropoff_datetime'])
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    return data

df = load_data()
st.markdown(" #### Let's show a sample of our data, to see what type of data we'll be dealing with.")
# Use checkboxes to show/hide data

if st.checkbox('Show dataframe'):
    st.dataframe(df.head(10))

st.markdown("****")

#VISUAL REPRESENTATIONS
st.subheader('Number of pickups by hour')
hist_values = np.histogram(df['tpep_pickup_datetime'].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)
st.line_chart(hist_values,use_container_width=True)

st.subheader('Number of dropoffs by hour')
hist_values = np.histogram(df['tpep_dropoff_datetime'].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)
st.line_chart(hist_values)

#Filtered hours on histograms
hour_to_filter = st.slider('hour', 0, 23, 17)  # min: 0h, max: 23h, default: 17h
filtered_data = df['tpep_dropoff_datetime'].dt.hour == hour_to_filter
st.subheader(f'Histograms of all pickups at {hour_to_filter}:00')
hist_values = np.histogram(filtered_data, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)
st.line_chart(df[['tpep_pickup_datetime','tpep_dropoff_datetime']])
#Some metrics
col1, col2 = st.columns(2)
col1.metric("Highest number of pickups", "70", "50")
col2.metric("Highest number of Dropoffs", "30", "20")

#Mapping data
#st.map(df)

#Top ten highest distance

