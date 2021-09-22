import streamlit as st
# importing numpy and pandas for to work with sample data.
import numpy as np
import pandas as pd 
import time

# Add text adn data 
st.title("News !")
st.sidebar.write("""
    # Streamlit app
    For dummies
""")

# Write a data Frame
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})
st.write(df)
  #or
st.table(df)

# Draw charts and maps
chart_data = pd.DataFrame( np.random.randn(20, 3), columns=['a', 'b', 'c'])
st.line_chart(chart_data)

# Plot a map
map_data = pd.DataFrame( np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4], columns=['lat', 'lon'])
st.map(map_data)

# Add interactivity with widgets

# Use checkboxes to show/hide data
if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame( np.random.randn(20, 3), columns=['a', 'b', 'c'])
chart_data

# Use a selectbox for options
option = st.selectbox('Which number do you like best?',df['second column'])
'You selected: ', option

# Lay out your app
option = st.sidebar.selectbox( 'Which number do you like best?', df['first column'])
'You selected:', option

# Lay out widgets side by side
left_column, right_column = st.columns(2)
pressed = left_column.button('Press me?')
if pressed:
    right_column.write("Woohoo!")
    expander = st.expander("FAQ")
    expander.write("Here you could put in some really, really long explanations...")

st.markdown("***")

# Create a progress bar
'Starting a long computation...'
# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
    # Update the progress bar with each iteration.
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)
'...and now we\'re done!'



