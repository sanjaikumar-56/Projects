# app.py
import streamlit as st
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
import pandas as pd
import os

# Load model
model = load_model("best_model.keras")  # or "best_model.keras"

# Load class labels
labels_df = pd.read_csv("d:/Milestone-3/traffic_signs_cleaned.csv")
class_labels = dict(zip(labels_df['ClassId'], labels_df['Name']))  # ✅ Use correct column names

# Image Preprocessing
def preprocess_image(image):
    image = image.convert('RGB')
    image = image.resize((64, 64))  # match model input size
    image = np.array(image) / 255.0
    image = np.expand_dims(image, axis=0)
    return image

# Streamlit UI
st.title("🚦 Traffic Sign Classifier")
st.write("Upload an image of a traffic sign, and the model will predict what it is.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    processed = preprocess_image(image)

    prediction = model.predict(processed)
    class_id = np.argmax(prediction)
    confidence = np.max(prediction)

    predicted_label = class_labels.get(class_id, "Unknown")  # use .get() for safe lookup

    st.markdown(f"### 🛑 Prediction: `{predicted_label}`")
    st.markdown(f"### 🔍 Confidence: `{confidence * 100:.2f}%`")

