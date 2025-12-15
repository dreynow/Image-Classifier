import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image

MODEL_PATH = "saved_models/happy_sad_classifier.h5"

def predict(image_path):
    model = load_model(MODEL_PATH)
    img = Image.open(image_path).resize((128,128))
    img_array = np.expand_dims(np.array(img)/255.0, axis=0)
    
    predictions = model.predict(img_array)
    class_index = np.argmax(predictions, axis=1)[0]
    confidence = np.max(predictions)
    
    print(f"Predicted class: {class_index}, Confidence: {confidence:.2f}")

if __name__ == "__main__":
    predict("src/img.jpeg")
