import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
import os

# Load the trained model
saved_model = load_model("model/braintumor.h5")

# Define tumor labels
labels = ['glioma_tumor', 'meningioma_tumor', 'no_tumor', 'pituitary_tumor']


def check(input_img):
    """Predicts the tumor type for the given image."""
    print("Your image is:", input_img)

    
    img_path = os.path.join("images", input_img)
    print("Full image path:", img_path)

    try:
        img = image.load_img(img_path, target_size=(150, 150))  # Load image
    except Exception as e:
        print("Error loading image:", e)
        return "Error: Unable to load image"  # Return an error message

    img = np.asarray(img) / 255.0  # Normalize image
    img = np.expand_dims(img, axis=0)  # Reshape for model

    output = saved_model.predict(img)
    predicted_index = np.argmax(output)  # Get index of highest probability
    predicted_class = labels[predicted_index]  # Map index to label

    print("Predicted tumor type:", predicted_class)
    return predicted_class  # Return predicted tumor type
