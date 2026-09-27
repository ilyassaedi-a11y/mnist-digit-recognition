import streamlit as st
import requests
from PIL import Image

st.set_page_config(layout="wide")
st.title("MNIST Digit Recognition")

col1, col2 = st.columns(2)

with col1:
    st.header("Upload Image")
    uploaded_file = st.file_uploader("Choose an image", type=['png', 'jpg', 'jpeg'])
    if uploaded_file:
        st.image(uploaded_file, width=200)

with col2:
    st.header("Prediction Result")
    if st.button("Predict Digit"):
        if uploaded_file:
            uploaded_file.seek(0)  # file pointer reset karna zaroori hai
            files = {"image": uploaded_file}
            response = requests.post("http://127.0.0.1:5000/predict", files=files)
            
            if response.status_code == 200:
                result = response.json()
                st.success("Prediction Complete!")
                st.write("### Predicted Digit")
                st.write(f"# {result['predicted_digit']}")
                st.write(f"Confidence: {result['confidence']*100:.2f}%")
            else:
                st.error("API se error aaya")
        else:
            st.warning("Pehle image upload karein")