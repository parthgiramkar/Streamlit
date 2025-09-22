import streamlit as st

st.title("Coffee Voting Poll")

coln1 , coln2 = st.columns(2)
with coln1 :

    st.write("Hot Coffee")
    st.image("https://www.scrs.in/uploads/members/file_ac8a298.jpg ",width=250)
    vote1 = st.button("Vote Hot Coffee")

with coln2 :
    st.write("Cold Coffee")
    vote2 = st.button("Vote Cold Coffee")

if vote1 :
    st.success("Thanks for voting Hot Coffee!")
if vote2 :
    st.success("Thanks for voting Cold Coffee!")



name =st.sidebar.text_input("Enter Your Name -")            
age = st.sidebar.text_input("Enter Your Age -")

with st.expander("About the App") :
    st.write("""
          1. This app allows users to vote for their favorite type of coffee.
          2. The results are displayed instantly after voting.
    """)


st.markdown('### Thanks For Voting')

st.markdown("> Enjoy Your Coffee")
st.markdown("> Visit Again")

st.caption("Developed by Coffee Lover")