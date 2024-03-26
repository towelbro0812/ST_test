import streamlit as st
import cv2
import numpy as np
from streamlit_modal import Modal

if "img_file_buffer" not in st.session_state:
    st.session_state.img_file_buffer = None

modal = Modal(
    "Camera Modal",
    key="camera_modal",  # Unique key for the modal  
    # Optional
    padding=20,    # default value
    max_width=744  # default value
)
if st.button("Open Camera"):
    modal.open()

if modal.is_open():
    with modal.container():
        st.session_state.img_file_buffer = st.camera_input("Take a picture")
    if st.session_state.img_file_buffer is not None:
        modal.close()


if st.session_state.img_file_buffer is not None:
    # To read image file buffer with OpenCV:
    bytes_data = st.session_state.img_file_buffer.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)

    # Check the type of cv2_img:
    # Should output: <class 'numpy.ndarray'>
    st.write(type(cv2_img))

    # Check the shape of cv2_img:
    # Should output shape: (height, width, channels)
    st.write(cv2_img.shape)