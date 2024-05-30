from fastapi import FastAPI, Request, UploadFile
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from tensorflow.python import keras
import model
import numpy as np

model.save('model_final.keras')
model_loaded = keras.models.load_model('model_final.keras')

app = FastAPI()
templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")



@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/upload")
def upload_page(request: Request):
    return templates.TemplateResponse("upload.html", {"request": request})


@app.get("/results")
def results_page(request: Request):
    return templates.TemplateResponse("results.html", {"request": request})


@app.post("/predict")
async def predict(file: UploadFile):
    contents = await file.read()
    return {"result": "Healthy"}


if __name__ == "__main__":
    app.run(debug=True)

