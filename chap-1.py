import streamlit as st

st.title("Coffe Maker App")
sug = st.checkbox("Add Sugar") 

if st.button("Make Coffe") :
    
    st.success("Your Coffe is being brewed")     
    if sug :
        st.write("Sugar has been Added")


kof_base = st.radio("Select Coeffe Base - ",["Hot milk","Cold Milk","Water"] )
st.write(f"Selected {kof_base} as your base")

flav = st.selectbox("Select Flavour",["Dark chocholate","Caramel","Mocha","Hazelnut"])

st.write("Selected Flavour {flav}")

amit = st.slider("Select Coeffe Strength(mg)",0,20,1)

st.number_input("No.of cups",min_value=1,max_value=10,step=1)

nam = st.text_input("Enter Your Name -")                 # same for date_input
if nam :
    st.text(f"{nam} your order is being prepared")