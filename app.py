import streamlit as st
import cv2
import numpy as np
from utils import preprocess_image, extract_text

st.set_page_config(page_title="Blue Text Revealer", layout="centered")
st.title("Reveal Hidden Text Behind Blue Marks")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    st.image(image, caption="Original Image", use_column_width=True)

    with st.spinner("Processing image..."):
        processed_img = preprocess_image(image)
        text = extract_text(processed_img)

    st.image(processed_img, caption="Processed Image", use_column_width=True)
    st.subheader("Extracted Text")
    st.text(text)