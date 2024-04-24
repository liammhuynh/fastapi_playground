import io
import requests
import shutil
from fastapi import FastAPI, UploadFile, File
from transformers import pipeline
from PIL import Image
from transformers import AutoImageProcessor, ResNetForImageClassification
import torch

app = FastAPI()

@app.post("/generate_caption/")
async def generate_caption_api(image: UploadFile = File(...)):
    # Read the image file
    contents = await image.read()    
    # Convert the binary data to an image
    image = Image.open(io.BytesIO(contents))
    caption = generate_caption_huggingface(image)
    return {"caption": caption}

def generate_caption_huggingface(image):
    captioner = pipeline("image-to-text",model="Salesforce/blip-image-captioning-base", max_new_tokens = 50)
    result = captioner(image)
    text = result[0]["generated_text"]
    return text
    
