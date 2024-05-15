import streamlit as st
import cv2
import tempfile
from st_pages import hide_pages
hide_pages('video')

st.title('Drone Detection System')

vf = st.file_uploader('Upload your desire Video',type=['mp4'])
if vf is None:
    st.write('File is missing')
else:
    tfile = tempfile.NamedTemporaryFile(delete=False)
    tfile.write(vf.read())
    cap = cv2.VideoCapture(tfile.name)

    stframe = st.empty()

    while cap.isOpened():
        ret,frame = cap.read()
        if not ret:
            print('cant open')
            break
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        stframe.image(gray)
