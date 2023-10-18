from fastapi import FastAPI
import requests
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
async def say_hello(url: str, x: int, y: int):
    image = requests.get(url)
    image = ml.getData(image)
    service.saveFile(image, x, y)
    return image
