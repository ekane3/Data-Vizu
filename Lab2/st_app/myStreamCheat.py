"""
Author : EKANE EMILE
github :  ekane3.github.io
Subject : Simple streamlit cheat sheet
"""

import streamlit as st
# importing numpy and pandas for to work with sample data.
import numpy as np
import pandas as pd 


st.sidebar.title("My StreamCheat")
st.echo(code_location='below')
st.write('This code will be printed')



"""
# Progress bar
'Hold on, loading...'
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    # Update the progress bar with each iteration.
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)
'...and now we\'re done!'
# delete bar after loading
bar.empty()
"""
















