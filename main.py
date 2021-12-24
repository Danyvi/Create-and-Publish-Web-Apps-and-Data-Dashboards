import streamlit as st
import pandas as pd

data = {
   'Series_1': [1,3,4,5,7],
   'Series_2': [10,30,40,100,250]
}

#create a dataframe from data
df = pd.DataFrame(data )

st.title('Our first Streamlit App')
st.subheader('Introducing Streamlit in Automate Everything with Python')
st.write('''This is our first Web App''')

st.write(df)