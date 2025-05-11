import streamlit as st

st.title("welcome  to the era of coding")
st.header("Selection of the langueage")

x = st.selectbox("Select the language", ["Python", "Java", "C++", "JavaScript"])
y = st.select_slider("your knowledge of {x}", ["20", "40", "60", "80", "100"])
st.multiselect("Select the language", ["Python", "Java", "C++", "JavaScript"])

st.success(f"language selected {x}" +" "+ f"your knowledge of {x} is {y}") 