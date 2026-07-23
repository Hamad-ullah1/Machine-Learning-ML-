import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np
import os

# Define the CIFAR-10 classes corresponding to the model outputs
CLASSES = ['Airplane', 'Automobile', 'Bird', 'Cat', 'Deer', 
           'Dog', 'Frog', 'Horse', 'Ship', 'Truck']

st.set_page_config(page_title="CIFAR-10 Image Classifier", page_icon="🖼️")

st.title("🖼️ CIFAR-10 Image Classifier (CNN)")
st.write("Upload an image, and this Convolutional Neural Network will predict which of the 10 CIFAR-10 classes it belongs to.")

@st.cache_resource
def load_cnn_model():
    # Make sure this points exactly to where you saved your Keras model!
    # E.g. in your Jupyter notebook, run: model.save("cifar10_model.keras")
    model_path = r"D:\NAVTTC-AI-Course\Month 02\Week 08\Notebooks\simpe_cnn_cifar10.keras"
    if os.path.exists(model_path):
        return tf.keras.models.load_model(model_path)
    else:
        return None

model = load_cnn_model()

if model is None:
    st.warning("⚠️ Model file not found! Please make sure to save your trained model from the notebook using `model.save('cifar10_model.keras')` and place it in this directory.")
else:
    st.success("✅ Model loaded successfully!")

    # Provide an interface to upload or drop an image
    uploaded_file = st.file_uploader("Choose an image to classify...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Load and display the image
        img = Image.open(uploaded_file)
        
        # Display the image neatly in a column layout
        col1, col2 = st.columns([1, 1])
        with col1:
            st.image(img, caption="Uploaded Image", use_column_width=True)

        with col2:
            st.write("### Analyzing...")
            # Preprocess the image to match the CIFAR-10 training scheme
            # 1. Resize to 32x32 pixels
            img_resized = img.resize((32, 32))
            
            # 2. Convert to numpy array and scale to [0, 1]
            img_array = np.array(img_resized).astype('float32') / 255.0
            
            # If the image happens to have an alpha channel (RGBA), convert to RGB
            if img_array.shape[-1] == 4:
                img_array = img_array[..., :3]
                
            # If it's grayscale, we need it to be 3 channels for CIFAR...
            if len(img_array.shape) == 2:
                img_array = np.stack((img_array,)*3, axis=-1)

            # 3. Add the batch dimension (1, 32, 32, 3)
            img_batch = np.expand_dims(img_array, axis=0)
            
            # 4. Predict
            predictions = model.predict(img_batch)
            predicted_class_index = np.argmax(predictions[0])
            confidence = predictions[0][predicted_class_index] * 100
            
            # Output Results
            st.metric(label="Predicted Class", value=CLASSES[predicted_class_index])
            st.write(f"**Confidence Score:** {confidence:.2f}%")
            
            # Optional: Show all class probabilities as a progress bar list
            with st.expander("Show detailed probabilities"):
                for i, class_name in enumerate(CLASSES):
                    st.write(f"{class_name}: {predictions[0][i]*100:.2f}%")
                    st.progress(float(predictions[0][i]))
