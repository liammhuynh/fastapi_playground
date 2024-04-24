Server-Client using FastAPI

This repo is my learning playground for implementing server-client apps using FastAPI.

If you want to try out the code, follow these steps:

Install Dependencies: Make sure to install the required dependencies using pip.

pip install -r requirements.txt

Run the Server: Execute the server using uvicorn.

uvicorn server:app --reload

Run the Client: Start the client by running the following command.

python3 client.py

Test via UI: Access the API documentation through a web browser.

Simply copy the HTTP address of the server and append '/docs' to it. For example:

http://127.0.0.1:8000/docs
