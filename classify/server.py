import io
import requests
import shutil
from fastapi import FastAPI, UploadFile, File
from transformers import pipeline
from PIL import Image
from transformers import AutoImageProcessor, ResNetForImageClassification
import torch

app = FastAPI()

@app.post("/classify_image/")
async def classify_image_api(image: UploadFile = File(...)):
    # Read the image file
    contents = await image.read()    
    # Convert the binary data to an image
    image = Image.open(io.BytesIO(contents))

    processor = AutoImageProcessor.from_pretrained("microsoft/resnet-50")
    model = ResNetForImageClassification.from_pretrained("microsoft/resnet-50")

    inputs = processor(image, return_tensors="pt")

    with torch.no_grad():
        logits = model(**inputs).logits

    # model predicts one of the 1000 ImageNet classes
    predicted_label = logits.argmax(-1).item()
    print(model.config.id2label[predicted_label])
    return {"class_label": model.config.id2label[predicted_label]}
    
