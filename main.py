from typing import Union

from fastapi import FastAPI
import manager.logmanager as logmanager
import manager.chat as chat

app = FastAPI()
logmgr = logmanager.LogManager()


@app.get("/")
def read_root():
    return "Hello, Taxim-Server!"


@app.get("/static-log")
def getlog_by_date(date: str, vcnt: int, tcnt: int):
    return logmgr.get_log_by_date(date, vcnt, tcnt)


@app.get("/static-log-timestamp")
def getlog_by_timestamp(date: str = '20200829', vcnt: int = 1, tcnt: int = 10, timestamp: int = 1675349880000):
    return logmgr.get_log_by_timestamp(date, vcnt, tcnt, timestamp)


@app.get("/static-log-timestamp-delta")
def getlog_by_timestamp_delta(date: str = '20200829', vcnt: int = 1, tcnt: int = 10, timestamp: int = 1675349880000, delta: int = 3):
    return logmgr.get_log_by_timestamp_delta(date, vcnt, tcnt, timestamp, delta)


@app.get("/static-schedule-timestamp")
def getschedule_by_timestamp(date: str = '20200829', vcnt: int = 1, tcnt: int = 10, timestamp: int = 1675349880000):
    return logmgr.get_schedule_by_timestamp(date, vcnt, tcnt, timestamp)


@app.get("/static-schedule-timestamp-delta")
def getschedule_by_timestamp_delta(date: str = '20200829', vcnt: int = 1, tcnt: int = 10, timestamp: int = 1675349880000, delta: int = 3):
    return logmgr.get_schedule_by_timestamp_delta(date, vcnt, tcnt, timestamp, delta)


@app.get("/chat")
def get_chat(text: str = "Hi Taxim"):
    return chat.hello(text)
