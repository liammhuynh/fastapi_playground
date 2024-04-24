import requests

def send_request_image(filename):
    url = "http://localhost:8000/generate_caption/"
    files = {"image": open(filename, "rb")}
    response = requests.post(url, files=files)
    print(response.json())
    
if __name__ == "__main__":
    image_path = "images/parrots.jpeg"
    send_request_image(image_path)

