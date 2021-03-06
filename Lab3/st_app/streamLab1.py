"""
Author : EKANE EMILE
github :  ekane3.github.io
Subject : Streamlit with Lab1
"""
import streamlit as st
# Streaming the first dataset
import numpy as np
import pandas as pd 
import time
import seaborn as sns
import plotly.figure_factory as ff
import matplotlib.pyplot as plt
import streamlit.components.v1 as components




#Title bar
def title_bar():
    st.sidebar.title("Currently streaming ❤")
    st.sidebar.markdown("Select the Charts/Plots accordingly:")
    project_title = st.sidebar.text_input("You can change the title of this project")
    if project_title:
        st.title(project_title)
    else:
        st.title("Uber raw data April 2014")
    st.sidebar.write("Made by [EKANE E. Emile](http://ekane3.github.io/ )")
    st.markdown("The dashboard will visualize Uber data of April 2014")
    st.markdown("Uber, is an American technology company. Its services include ride-hailing, food delivery, package delivery, couriers, freight transportation, and, through a partnership with Lime, electric bicycle and motorized scooter rental.")
    st.write("""
    ### Details of the dataset:
    *The dataset contains information about the Datetime, Latitude, Longitude and Base of each uber ride that happened in the month of July 2014 at New York City, USA.*

    Date/Time : The date and time of the Uber pickup  
    Lat : The latitude of the Uber pickup  
    Lon : The longitude of the Uber pickup  
    Base : The TLC base company code affiliated with the Uber pickup

    The Base codes are for the following Uber bases:  
    B02512 : Unter  
    B02598 : Hinter  
    B02617 : Weiter  
    B02682 : Schmecken  
    B02764 : Danach-NY  
    """)
title_bar()
#LOAD DATA
#Connecting to endpoint to get csv file 

DATA_URL = ("uber-raw-data-apr14.csv")

# Function to load data
@st.cache(allow_output_mutation=True)
def load_data(): 
    data = pd.read_csv(DATA_URL)
    #Convert date/time column type from object to datetime
    data['Date/Time'] = pd.to_datetime(data['Date/Time'])
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    return data
#Loading data in dataFrame
df = load_data()

#Functions to get day of month, weekday, hour

def get_dom(dt):
    return dt.day
df['dom'] = df['date/time'].map(get_dom)

def get_weekday(dt):
    return dt.weekday()
df['weekday'] = df['date/time'].map(get_weekday)

def get_hour(dt):
    return dt.hour
df['hour'] = df['date/time'].map(get_hour)

# Show a sample of our data

def show_head():
    st.markdown(" #### Let's show a sample of our data, to see what type of data we'll be dealing with.")
    if st.checkbox('Show dataframe'):
        st.table(df.head(10))

show_head()


#hist_values = np.histogram(df[], bins=24, range=(0,24))[0]
#st.bar_chart(hist_values)
#st.bar_chart(df['dom'])
#st.line_chart(df)

#VISUAL REPRESENTATION

def histograms():
    st.subheader('Frequency by date of month')

    #st.dataframe(df.head())
    #some space
    st.markdown("***")
    st.subheader('Histograms of Longitude and latitude')
    fig, ax = plt.subplots(1,2)
    ax[0].hist(df['lat'], bins=60,color='orchid')
    ax[1].hist(df['lon'], bins=60,color='yellow',edgecolor = 'red')
    st.pyplot(fig)
histograms()

#COUNTS

def counts_visu():
    st.write(df['lon'].value_counts())
    st.write(df['lat'].value_counts())

    st.header("Number of pickups per base")
    st.set_option('deprecation.showPyplotGlobalUse', False)
    plt.figure(figsize=(10,10))
    fig = sns.countplot(y = df['base'])
    st.pyplot()

counts_visu()

# Maps

def maps_visu():
    st.subheader("Mapping the dataset ")
    st.map(df.head(50))

maps_visu()
# bootstrap 4 collapse example
components.html(
    """
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
    <div id="accordion">
      <div class="card">
        <div class="card-header" id="headingOne">
          <h5 class="mb-0">
            <button class="btn btn-link" data-toggle="collapse" data-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
            Some images of the project
            </button>
          </h5>
        </div>
        <div id="collapseOne" class="collapse show" aria-labelledby="headingOne" data-parent="#accordion">
          <div class="card-body">
            nothing for the moment , come later
          </div>
        </div>
      </div>
      <div class="card">
        <div class="card-header" id="headingTwo">
          <h5 class="mb-0">
            <button class="btn btn-link collapsed" data-toggle="collapse" data-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">
            Testing Streamlit components
            </button>
          </h5>
        </div>
        <div id="collapseTwo" class="collapse" aria-labelledby="headingTwo" data-parent="#accordion">
          <div class="card-body">
            nothing for the moment , come later
          </div>
        </div>
      </div>
    </div>
    """,
    height=300,
)
