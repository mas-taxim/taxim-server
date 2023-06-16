from typing import Union

from fastapi import FastAPI, Query, Path
from fastapi.middleware.cors import CORSMiddleware

import manager.logmanager as logmanager
import manager.chat as chat
from manager.time import transform
# import mvs.mvs as mvs

from datetime import datetime


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

logmgr = logmanager.LogManager()


@app.get("/")
def read_root():
    return "Hello, Taxim-Server!"


@app.get("/log/{date}")
def getlog_by_date(
        date: str = Path(..., description='yyyymmdd'),
        vehicles: int = Query(1),
        tasks: int = Query(10)):
    return logmgr.get_log_by_date(date, vehicles, tasks)


'''
@app.get("/log/timestamp/{date}")
def getlog_by_timestamp(
    date: str = Path(..., description='yyyymmdd'),
    vehicles: int = Query(1),
    tasks: int = Query(10),
    timestamp: str = Query('1675349880000')
    ):
    return logmgr.get_log_by_timestamp(date, vehicles, tasks, timestamp)
'''


@app.get("/log/{yyyy}/{mm}/{dd}/{hh}/{mi}")
def getlog_by_timestamp(
        yyyy: int = Path(..., description='yyyy'),
        mm: int = Path(..., description='mm'),
        dd: int = Path(..., description='dd'),
        hh: int = Path(..., description='hh'),
        mi: int = Path(..., description='mi'),
        vehicles: int = Query(1),
        tasks: int = Query(10)):

    # dt = datetime(yyyy, mm, dd, hh, mi, 00)
    # date = dt.strftime("%Y%m%d")
    # timestamp = dt.timestamp() * 1000
    date, timestamp = transform(yyyy, mm, dd, hh, mi)

    return logmgr.get_log_by_timestamp(date, vehicles, tasks, timestamp)


@app.get("/log-delta/{yyyy}/{mm}/{dd}/{hh}/{mi}")
def getlog_by_timestamp_delta(
        yyyy: int = Path(..., description='yyyy'),
        mm: int = Path(..., description='mm'),
        dd: int = Path(..., description='dd'),
        hh: int = Path(..., description='hh'),
        mi: int = Path(..., description='mi'),
        vehicles: int = Query(1),
        tasks: int = Query(10),
        delta: int = Query(..., description="delta")):

    date, timestamp = transform(yyyy, mm, dd, hh, mi)
    return logmgr.get_log_by_timestamp_delta(date, vehicles, tasks, timestamp, delta)


'''
@app.get("/schedule/timestamp/{date}")
def getschedule_by_timestamp(
        date: str = Path(...),
        vehicles: int = Query(1),
        tasks: int = Query(10),
        timestamp: str = Query('1675349880000')):

    return logmgr.get_schedule_by_timestamp(date, vehicles, tasks, timestamp)
'''


@app.get("/schedule/{yyyy}/{mm}/{dd}/{hh}/{mi}")
def getschedule_by_timestamp(
        yyyy: int = Path(..., description='yyyy'),
        mm: int = Path(..., description='mm'),
        dd: int = Path(..., description='dd'),
        hh: int = Path(..., description='hh'),
        mi: int = Path(..., description='mi'),
        vehicles: int = Query(1),
        tasks: int = Query(10)):

    date, timestamp = transform(yyyy, mm, dd, hh, mi)

    return logmgr.get_schedule_by_timestamp(date, vehicles, tasks, timestamp)


'''
@app.get("/schedule/timestamp-delta/{date}")
def getschedule_by_timestamp_delta(
        date: str = Path(...),
        vehicles: int = Query(1, description='vehicle count'),
        tasks: int = Query(10),
        timestamp: str = Query('1675349880000'),
        delta: int = Query(3)):
    return logmgr.get_schedule_by_timestamp_delta(date, vehicles, tasks, timestamp, delta)
'''


@app.get("/schedule-delta/{yyyy}/{mm}/{dd}/{hh}/{mi}")
def getschedule_by_timestamp_delta(
        yyyy: int = Path(..., description='yyyy'),
        mm: int = Path(..., description='mm'),
        dd: int = Path(..., description='dd'),
        hh: int = Path(..., description='hh'),
        mi: int = Path(..., description='mi'),
        vehicles: int = Query(1),
        tasks: int = Query(10),
        delta: int = Query(..., description='Delta')):

    date, timestamp = transform(yyyy, mm, dd, hh, mi)

    return logmgr.get_schedule_by_timestamp_delta(date, vehicles, tasks, timestamp, delta)


@app.get("/chat")
def get_chat(text: str = "Hi Taxim"):
    return chat.hello(text)


'''
@app.get("/run-simulator")
def run_simulator(vehicles: int = Query(...), tasks: int = Query(...)):
    mvs.run(vehicle_num=vehicles, task_num=tasks)
    return "Complete"
'''
