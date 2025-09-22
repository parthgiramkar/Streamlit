import streamlit as st
import pandas as pd

st.markdown("# Coffee Sales Dashboard")
file = st.file_uploader("Upload your csv file", type=["csv","json"])

if file :
    df = pd.read_csv(file)
    st.subheader("Data Preview ")
    st.dataframe(df)

if file :
    st.subheader("Statistical Summary")
    st.table(df.describe())

if file :
    k = df['City'].unique()
    st.markdown("#  Sales across City")
    
    city  = st.selectbox("Select City",k)
    df_city = df[df["City"] == city ]

    st.dataframe(df_city)