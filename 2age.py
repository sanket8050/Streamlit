import streamlit as st
from datetime import datetime

st.title("🎂 Age Calculator")

# Ask user for DOB
dob = st.date_input("Enter your Date of Birth")

# Get current datetime
now = datetime.now()

# Convert dob to datetime
dob_datetime = datetime.combine(dob, datetime.min.time())

# Calculate time difference
diff = now - dob_datetime

# Total seconds, minutes, hours
total_seconds = int(diff.total_seconds())
total_minutes = total_seconds // 60
total_hours = total_minutes // 60
total_days = diff.days


# Rough estimate of years, months, days
years = total_days // 365
remaining_days = total_days % 365
months = remaining_days // 30
days = remaining_days % 30

# Show results
if st.button("Calculate Age"):
    st.write(f"Your age is approximately {years} years, {months} months, and {days} days.")
    st.write(f"Total seconds: {total_seconds}")
    st.write(f"Total minutes: {total_minutes}")
    st.write(f"Total hours: {total_hours}")
    st.write(f"Total days: {total_days}")
   
    st.balloons()
