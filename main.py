# def main():
#     print("Hello from coeffe-streamlit!")


# if __name__ == "__main__":
#     main()

import streamlit as st
st.title("Hello Coffe Lovers!")

st.subheader("Strongly Brewed with streamlit")
st.text("Welcome to Our Coeffe Web App")

st.write("Choose your fav. type of coffee ")

kof = st.selectbox("Menu - " ,["Black coeffe","Latte","Cappuccino","Cold coeffe"] ) 

st.write(f"You choosed {kof} .Excelletent choice!")

st.success(f"Your {kof} has been Brewed")