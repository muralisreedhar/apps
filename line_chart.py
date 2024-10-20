import streamlit as st
import pandas as pd
import numpy as np


# list of name, degree, score
assess = ["Health History Assessment", "Auditory Processing Test", "Social Communication"]
year = ["2010", "2013", "2016"]
score = [90, 40, 80, 98]
 
# dictionary of lists 
dict = {'category': assess, 'year': year, 'score': score} 
   
df = pd.DataFrame(dict)

st.line_chart(df, x="year", y="category", color="score")
