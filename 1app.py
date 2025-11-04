import streamlit as st
import plotly.graph_objects as go

st.title("Plotly Test")

fig = go.Figure()
fig.add_trace(go.Scatter(y=[1, 3, 2, 4]))
st.plotly_chart(fig)
