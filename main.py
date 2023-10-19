import json
import pandas as pd
from PIL import Image
from loguru import logger
import sys

from io import BytesIO

from fastapi import FastAPI, File, status, UploadFile
from fastapi.responses import RedirectResponse
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import HTTPException

# logger

logger.remove()
logger.add(
    sys.stderr,
    colorize=True,
    format="<green>{time:HH:mm:ss}</green> | <level>{message}</level>",
    level=10,
)
logger.add("log.log", rotation="1 MB", level="DEBUG", compression="zip")

# FastAPI Setup

app = FastAPI(
    title="Detection Road Defects API",
    description="""Obtain object value out of image
                    and return image and json result""",
    version="2023.1.31",
)

class IDbService:
    def saveFile(self, data, x, y):
        pass

    def getPoints(self):
        pass

class IMlService:
    def getData(self, image):
        pass

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
