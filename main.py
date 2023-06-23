import os
from typing import Union

from fastapi import FastAPI, Query, Path, Body
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

from simul import router as SimulatorRouter

app = FastAPI(
    title="Taxim Backend Server",
    description="posible : 2020/08/29/**/**, (vehiclenum, tasks) : (1, 10), (2, 20)",
    version="1.0.0")

# CORS 미들웨어 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 허용할 웹 페이지의 출처
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root_page():
    return FileResponse(os.path.join('front', 'index.html'))


app.mount("/", StaticFiles(directory="front"), name="front")
app.include_router(SimulatorRouter, prefix="/api", tags=["simulator"])
