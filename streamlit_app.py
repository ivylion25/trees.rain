import av.frame
import cv2
import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoHTMLAttributes
import numpy as np
import av

def transform(frame: av.VideoFrame):
    img = frame.to_ndarray(format="bgr24")
    if flip_image:
        img = cv2.flip(img, 1)
    return av.VideoFrame.from_ndarray(img, format="bgr24")

#if take is not None:

img_file_buffer = st.camera_input("Take a picture")
flip_image = st.checkbox("Flip the image", True)
if img_file_buffer is not None:
    # To read image file buffer with OpenCV:
    bytes_data = img_file_buffer.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
    color_converted = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2RGB)
    if flip_image:
    # Check the type of cv2_img:
    # Should output: <class 'numpy.ndarray'>
        cv2_img = cv2.flip(cv2_img, 1)
    
    color_converted = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2RGB)


    # Check the shape of cv2_img:
    # Should output shape: (height, width, channels)
    st.write(cv2_img.shape)
    st.image(color_converted)

webrtc_streamer(key="streamer", video_frame_callback=transform, sendback_audio=False, )
