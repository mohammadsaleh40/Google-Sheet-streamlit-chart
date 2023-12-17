import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

sheet_id = "1vIV2Sl1Mad9e-lf24-iVqXs6gwuRij-bOUl7Iir2hQ8"
df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")

fig1 = px.line(df, x='y', y='x2', color='x3' ,animation_frame='x1')
st.plotly_chart(fig1, use_container_width=True)

fig2 = px.line(df, x='x3', y='x2' ,color='y' ,animation_frame='x1')
fig2['layout']['yaxis'].update(autorange = True)
st.plotly_chart(fig2, use_container_width=True)