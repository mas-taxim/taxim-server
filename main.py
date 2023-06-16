from typing import Union

from fastapi import FastAPI
import manager.logmanager as logmanager

app = FastAPI()
logmgr = logmanager.LogManager()


@app.get("/")
def read_root():
    return "Hello, Taxim-Server!"


@app.get("/static-log")
def getlog(date: str, vcnt: int, tcnt: int):
    return logmgr.get_log_by_date(date, vcnt, tcnt)


@app.get("/static-log-timestamp")
def getlog(date: str, vcnt: int, tcnt: int, timestamp: int):
    return logmgr.get_log_by_timestamp(date, vcnt, tcnt, timestamp)


@app.get("/static-log-timestamp-delta")
def getlog(date: str, vcnt: int, tcnt: int, timestamp: int, delta: int):
    print(type(delta))
    return logmgr.get_log_by_timestamp_delta(date, vcnt, tcnt, timestamp, int(delta))
