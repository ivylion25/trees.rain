import streamlit as st
import cv2
import numpy as np

#take = st.camera_input("Take a picture")


#if take is not None:

img_file_buffer = st.camera_input("Take a picture")

if img_file_buffer is not None:
    # To read image file buffer with OpenCV:
    bytes_data = img_file_buffer.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)

    # Check the type of cv2_img:
    # Should output: <class 'numpy.ndarray'>
    cv2_img = cv2.flip(cv2_img, 1)
    color_converted = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2RGB)


    # Check the shape of cv2_img:
    # Should output shape: (height, width, channels)
    st.write(cv2_img.shape)
    st.image(color_converted)

