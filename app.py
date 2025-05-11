import streamlit as st 
# title
st.title("Welcome to interactive streamlit app")

# header
st.header("Machine Learning Model")

# subheader
st.subheader("This is a subheader")

# text
st.text("This is a text")

# markdown
st.markdown("This is a markdown")

# code
st.code("print('Hello World')")

# latex
st.latex(r''' a^2 + b^2 = c^2 ''')

# write
st.write("This is a write function")

# json
st.json({"name": "John", "age": 30, "city": "New York"})

# dataframe
import pandas as pd 
import numpy as np
df = pd.DataFrame(np.random.randn(10, 5), columns=list("ABCDE"))
st.dataframe(df)

# table
st.table(df)

# image
from PIL import Image
image = Image.open("C:/Users/ASUS/Pictures/S.PHOTORED.JPG")
st.image(image, caption="This is an image",  use_container_width=200 )

# video
video_file = open("C:/Users/ASUS/Videos/model architecature and further.mp4", "rb")
video_bytes = video_file.read()
st.video(video_bytes)   

# audio
audio_file = open("C:/Users/ASUS/Downloads/WhatsApp Audio 2025-05-04 at 13.57.09_9d703e6b.mp3", "rb")
audio_bytes = audio_file.read() 
st.audio(audio_bytes)

# checkbox
if st.checkbox("Show dataframe"):
    st.write(df)

        

