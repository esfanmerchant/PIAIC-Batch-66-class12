import streamlit as st
from PIL import Image

# Load and display an image
# Make sure "streamlit.png" is in the same directory as your script
# img = Image.open("streamlit.png")
# st.image(img, width=400)

# Button to count clicks
btn = st.button("Click me")

if "count" not in st.session_state:
    st.session_state.count = 0

if btn:
    st.session_state.count += 1
    st.write(f"Button clicked {st.session_state.count} times")

# Chat input
chat_input = st.chat_input("Enter Your Prompt")

if chat_input:
    st.chat_message("user").write(chat_input)
    st.chat_message("assistant").write("Hello, how can I help you today?")