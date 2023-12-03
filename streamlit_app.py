
import streamlit as st
import pandas as pd
 
st.write("""
# China National Economic Growth Forcasting *system* 
""")
 
df = pd.read_csv("ChinaNationalEconomyData.csv")
st.line_chart(df)