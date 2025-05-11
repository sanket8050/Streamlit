import streamlit as st

st.title("make your chai")
if st.button("make chai"):
    st.balloons()
    st.snow()

    

st.write("select the ingredients")
st.selectbox("Select the ingredients", ["water", "milk", "sugar", "tea powder"])
st.select_slider("Select the quantity", ["1 cup", "2 cup", "3 cup", "4 cup"])
st.multiselect("Select the ingredients", ["water", "milk", "sugar", "tea powder"])
st.number_input("Enter the quantity", min_value=1, max_value=10, value=1)
st.success("chai is ready") 
st.balloons()
st.snow()
