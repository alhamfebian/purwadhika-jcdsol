import streamlit as st
import pandas as pd

df = pd.read_csv('melb_data.csv')

st.write('Aplikasi Streamlit Pertama!')

st.dataframe(
    data = df
)