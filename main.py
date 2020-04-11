from fastapi import FastAPI
import cv2
from matplotlib import pyplot as plt

app = FastAPI()

#domain where this api is hosted for example : localhost:5000/docs to see swagger documentation automagically generated.


@app.get("/")
def home():
    return {"message":"Hello TutLinks.com"}
def show():
    im=cv2.imread('image0.png')
    plt.imshow(im)
    return 
    
