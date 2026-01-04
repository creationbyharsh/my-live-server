import streamlit as st
import os

st.title("My YouTube Live Server")

STREAM_KEY = st.text_input("YouTube Stream Key")

if st.button("Start Live"):
    os.system(f"ffmpeg -re -stream_loop -1 -i video.mp4 -c:v copy -c:a aac -f flv rtmp://a.rtmp.youtube.com/live2/{STREAM_KEY}")
