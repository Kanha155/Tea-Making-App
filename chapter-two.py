import streamlit as st
st.title("Tea Making App")
if st.button("Make Tea"):
    st.success(f"Your tea is brewed ...")
if st.checkbox("add Masala"):
    st.write(f"Masala added in the tea")
Base = st.radio("Pick your Tea Base :",["Milk","Almond Milk","Water"])
st.write(f"Selected Base as {Base}")
flavour=st.selectbox("Check Flavour:",["Select","Kesar","Adrak","Special","Simple"])
st.write(f"Selected Flavour {flavour}")
st.slider("Sugar Level (as Per Spoon)",0,6,4)
cups=st.number_input("How many Cups",min_value=1,max_value=10,step=1)
st.write(f"Selected cups quantity {cups}")

name = st.text_input("Enter your name")
if name:
    st.write(f"Welcome,{name} ! Your chai is on the way")

dob = st.date_input("Select your date of birth")
st.write(f"Your date of birth {dob}")