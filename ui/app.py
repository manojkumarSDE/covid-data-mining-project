import streamlit as st
import pandas as pd

st.title("COVID-19 Data Mining Dashboard")

clustered = pd.read_csv("../outputs/clustered_data.csv")
age_data = pd.read_csv("../outputs/age_mortality.csv", header=None)

st.header("Top 10 Affected Countries")
st.table(clustered.sort_values(by="Confirmed", ascending=False).head(10))

st.header("Mortality Rate by Age Group")
st.bar_chart(age_data.set_index(0))
