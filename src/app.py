from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
import io

MODEL_PATH = "saved_models/happy_sad_classifier.h5"

app = FastAPI(title="Image Classification API")

# Load model ONCE at startup
model = load_model(MODEL_PATH)

@app.get("/")
def health_check():
    return {"status": "ok"}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:
        # Read image from request
        image_bytes = await file.read()
        img = Image.open(io.BytesIO(image_bytes)).convert("RGB")
        img = img.resize((128, 128))

        # Preprocess
        img_array = np.expand_dims(np.array(img) / 255.0, axis=0)

        # Predict
        predictions = model.predict(img_array)
        class_index = int(np.argmax(predictions, axis=1)[0])
        confidence = float(np.max(predictions))

        return JSONResponse({
            "class_index": class_index,
            "confidence": round(confidence, 4)
        })

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": str(e)}
        )
