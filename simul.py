from typing import Union

from fastapi import FastAPI, Query, Path, Body
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi import APIRouter

import manager.logmanager as logmanager
import manager.chat as chat
from manager.time import transform
# import mvs.mvs as mvs

from datetime import datetime
from logger import logger

logmgr = logmanager.LogManager()


router = APIRouter()


@router.get("/log/{date}")
def getlog_by_date(
        date: str = Path(..., description='yyyymmdd'),
        vehicles: int = Query(1),
        tasks: int = Query(10)):
    return logmgr.get_log_by_date(date, vehicles, tasks)


'''
@router.get("/log/timestamp/{date}")
def getlog_by_timestamp(
    date: str = Path(..., description='yyyymmdd'),
    vehicles: int = Query(1),
    tasks: int = Query(10),
    timestamp: str = Query('1675349880000')
    ):
    return logmgr.get_log_by_timestamp(date, vehicles, tasks, timestamp)
'''


@router.get("/log/{yyyy}/{mm}/{dd}/{hh}/{mi}")
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


@router.get("/log-delta/{yyyy}/{mm}/{dd}/{hh}/{mi}")
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
@router.get("/schedule/timestamp/{date}")
def getschedule_by_timestamp(
        date: str = Path(...),
        vehicles: int = Query(1),
        tasks: int = Query(10),
        timestamp: str = Query('1675349880000')):

    return logmgr.get_schedule_by_timestamp(date, vehicles, tasks, timestamp)
'''


@router.get("/schedule/{yyyy}/{mm}/{dd}/{hh}/{mi}")
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
@router.get("/schedule/timestamp-delta/{date}")
def getschedule_by_timestamp_delta(
        date: str = Path(...),
        vehicles: int = Query(1, description='vehicle count'),
        tasks: int = Query(10),
        timestamp: str = Query('1675349880000'),
        delta: int = Query(3)):
    return logmgr.get_schedule_by_timestamp_delta(date, vehicles, tasks, timestamp, delta)
'''


@router.get("/schedule-delta/{yyyy}/{mm}/{dd}/{hh}/{mi}")
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


@router.post("/chat")
def send_chat_message(
        text: str = Body("Hi Taxim")):
    logger.debug(text)
    response: dict = chat.response(text)
    text = response.get('text')
    focus = response.get('focus')
    result = dict(text=text, action='nothing', data=None)
    if focus:
        result['action'] = 'focus'
        result['data'] = focus
    return result


'''
@router.get("/run-simulator")
def run_simulator(vehicles: int = Query(...), tasks: int = Query(...)):
    mvs.run(vehicle_num=vehicles, task_num=tasks)
    return "Complete"
'''
