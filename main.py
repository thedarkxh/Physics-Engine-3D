import streamlit as st
import numpy as np
import pandas as pd

st.title("JEE Physics: Projectile Motion Simulator")

u = st.slider("Initial Velocity (m/s)", 1, 100, 25)
theta = st.slider("Angle (degrees)", 1, 90, 45)

t_flight = (2 * u * np.sin(np.radians(theta))) / 9.8
t = np.linspace(0, t_flight, 100)
x = u * np.cos(np.radians(theta)) * t
y = u * np.sin(np.radians(theta)) * t - 0.5 * 9.8 * t**2

# Streamlit has its own built-in line chart that doesn't need Matplotlib's DLLs
chart_data = pd.DataFrame({'Horizontal': x, 'Vertical': y})
st.line_chart(chart_data.set_index('Horizontal'))