import requests
    
def send_classify(filename):
    url = "http://localhost:8000/classify_image/"
    files = {"image": open(filename, "rb")}
    response = requests.post(url, files=files)
    print(response.json())

if __name__ == "__main__":
    image_path = "images/parrots.jpeg"
    send_classify(image_path)

