import streamlit as st
import pandas as pd

tree_height = [1.2, 1.3, 1.3, 1.3, 1.4, 1.6, 1.9, 1.9, 1.95]
daily_rain = [.2, .1, 0, 0, .1, .2, .3, 0, .05]
n = pd.DataFrame()
n["tree height"] = tree_height
n["rain"] = daily_rain
st.title("Tree height by daily Rain")
st.line_chart(n, x_label="days", y_label="inches")
