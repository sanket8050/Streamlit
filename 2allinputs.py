import streamlit as st
from datetime import datetime

st.title("🌟 Streamlit Input Widgets Demo")

st.header("🧾 Text Inputs")
name = st.text_input("Enter your name")
bio = st.text_area("Tell us about yourself")

st.header("📅 Date & Time")
dob = st.date_input("Select your Date of Birth")
born_time = st.time_input("Select time of birth")

st.header("🔢 Numbers & Sliders")
age = st.number_input("Enter your age", min_value=0, max_value=120)
rating = st.slider("Rate this app", 1, 10)
size = st.select_slider("Choose T-shirt size", options=["S", "M", "L", "XL"])

st.header("✅ Boolean & Selection")
subscribe = st.checkbox("Subscribe to newsletter")
gender = st.radio("Select Gender", options=["Male", "Female", "Other"])
city = st.selectbox("Select your city", options=["Pune", "Mumbai", "Delhi", "Bangalore"])
fav_fruits = st.multiselect("Select your favorite fruits", ["Apple", "Banana", "Mango", "Orange"])

st.header("🗂️ File & Camera")
file = st.file_uploader("Upload a file (PDF, Image, CSV...)")
photo = st.camera_input("Take a selfie 📷")

st.header("🎨 Color Picker")
fav_color = st.color_picker("Pick your favorite color")

st.header("📋 Form Example")
with st.form("form1"):
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    submitted = st.form_submit_button("Login")
    if submitted:
        st.success(f"Welcome, {username}!")

st.header("🚀 Button")
if st.button("Click to Celebrate 🎉"):
    st.balloons()

# Output Summary
st.markdown("---")
st.subheader("📝 Summary of Your Input")
st.write(f"👤 Name: {name}")
st.write(f"🧾 Bio: {bio}")
st.write(f"📅 DOB: {dob}, 🕒 Time: {born_time}")
st.write(f"🔢 Age: {age}, Rating: {rating}, Size: {size}")
st.write(f"✅ Subscribed: {subscribe}, Gender: {gender}")
st.write(f"🏙️ City: {city}, Fruits: {fav_fruits}")
st.write(f"🎨 Favorite Color: {fav_color}")
