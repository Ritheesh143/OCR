from fastapi import FastAPI, Request, File
import pytesseract
import io

from PIL import Image

# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
pytesseract.pytesseract.tesseract_cmd = '/app/.apt/usr/bin/tesseract'


app = FastAPI()

@app.get("/")
def Welcome():
    return "Working"


@app.post("/img2str")
def Converter(file:bytes = File()):
    image = Image.open(io.BytesIO(file))
    return pytesseract.image_to_string(image)



@app.post("/batchimg2str")
def Batchconverter(file:bytes = File()):
    image = Image.open(io.BytesIO(file))
    return pytesseract.image_to_string(image)