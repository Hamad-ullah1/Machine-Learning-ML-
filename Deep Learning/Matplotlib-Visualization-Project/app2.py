import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np
import os

# Define the Chest CT-Scan classes corresponding to the model outputs
CLASSES = ['Adenocarcinoma', 'Large Cell Carcinoma', 'Normal', 'Squamous Cell Carcinoma']

st.set_page_config(page_title="Chest CT Scan Classifier", page_icon="🫁")

st.title("🫁 Chest CT Scan Medical Classifier")
st.write("Upload a Chest CT Scan image, and the deep neural network will predict whether it is normal or detects one of the lung cancer categories.")

@st.cache_resource
def load_cnn_model():
    # Load the Transfer Learning model trained on medical CT scans
    model_path = r"E:\NAVTTC-AI-Course\Month 02\Week 08\Notebooks\transfer_learning_mobilenetv2.keras"
    if os.path.exists(model_path):
        return tf.keras.models.load_model(model_path)
    else:
        # Fallback to ct_model as requested by user manually earlier
        fallback_path = r"E:\NAVTTC-AI-Course\Month 02\Week 08\Notebooks\ct_model.keras"
        if os.path.exists(fallback_path):
            return tf.keras.models.load_model(fallback_path)
        return None

model = load_cnn_model()

if model is None:
    st.warning("⚠️ Model file not found! Please make sure to save your trained model from the notebook and place it in the designated directory as a `.keras` file.")
else:
    st.success("✅ Model loaded successfully!")

    # Provide an interface to upload or drop an image
    uploaded_file = st.file_uploader("Choose a Chest CT Scan image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Load and display the image
        img = Image.open(uploaded_file)
        
        # Display the image neatly in a column layout
        col1, col2 = st.columns([1, 1])
        with col1:
            st.image(img, caption="Uploaded CT Scan", use_column_width=True)

        with col2:
            st.write("### Analyzing...")
            # Preprocess the image to match the Medical Transfer Learning training scheme
            # 1. Resize to 224x224 pixels (Default for MobileNet/ResNet/VGG)
            img_resized = img.resize((224, 224))
            
            # 2. Convert to numpy array and scale to [0, 1]
            img_array = np.array(img_resized).astype('float32') / 255.0
            
            # If the image happens to have an alpha channel (RGBA), convert to RGB
            if img_array.shape[-1] == 4:
                img_array = img_array[..., :3]
                
            # If it's grayscale, we need it to be 3 channels for Transfer Learning models...
            if len(img_array.shape) == 2:
                img_array = np.stack((img_array,)*3, axis=-1)

            # 3. Add the batch dimension (1, 224, 224, 3)
            img_batch = np.expand_dims(img_array, axis=0)
            
            # 4. Predict
            predictions = model.predict(img_batch)
            predicted_class_index = np.argmax(predictions[0])
            confidence = predictions[0][predicted_class_index] * 100
            
            # Output Results
            color = "red" if CLASSES[predicted_class_index] != "Normal" else "green"
            st.markdown(f"**Predicted Class:** <span style='color:{color}; font-size:24px; font-weight:bold;'>{CLASSES[predicted_class_index]}</span>", unsafe_allow_html=True)
            st.write(f"**Confidence Score:** {confidence:.2f}%")
            
            # Show all class probabilities as a progress bar list
            with st.expander("Show detailed probabilities"):
                for i, class_name in enumerate(CLASSES):
                    st.write(f"{class_name}: {predictions[0][i]*100:.2f}%")
                    st.progress(float(predictions[0][i]))
