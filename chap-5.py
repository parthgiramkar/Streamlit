import streamlit as st

import requests

st.title("Live Currency Converter ")

given = st.number_input("Enter amount in INR ", min_value=1)

curr = st.selectbox("Convert INR TO ",["USD","EUR","GBP","JPY","AUD","FJD"] )

if st.button("Convert") :

    url_link= "https://api.exchangerate-api.com/v4/latest/INR"

    resp = requests.get(url_link)

    if(resp.status_code == 200) :

        json_data = resp.json()
        value = json_data["rates"][curr]

        conv_amt = value*given

        st.success(f"{given} INR = {conv_amt} {curr}" )

    else :

        st.error("Failed to fetch data")