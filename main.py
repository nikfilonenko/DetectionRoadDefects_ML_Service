from fastapi import FastAPI, File, UploadFile
import numpy as np
import cv2
app = FastAPI()

class IDbService:
    def saveFile(self, data, x, y):
        ...

    def getPoints(self):
        ...

class IMlService:
    def getData(self, image):
        ...

service = IDbService()
ml = IMlService

@app.get("/")
async def root():
    points = service.getPoints()
    return points


@app.post("/")
async def post(x: int, y: int, image: UploadFile = File(...)):
    image = cv2.imdecode(np.frombuffer(image.file.read(), np.uint8), -1)
    image = ml.getData(image)
    service.saveFile(image, x, y)
    return image
