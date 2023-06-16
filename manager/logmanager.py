import json
import os
import sys


class LogManager:
    def __init__(self):
        self.log_container: dict[str, dict] = dict()

    def is_unloaded_date(self, date: str) -> bool:
        return not date in self.log_container

    def getKey(self, date: str, vnum: str, tnum: str):
        return f"{date}{vnum}{tnum}"

    def readLog(self, date: str, vnum: str, tnum: str):
        key = self.getKey(date, vnum, tnum)
        if not self.is_unloaded_date(key):
            return

        read_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'log', f'{date}_{vnum}_{tnum}.json')
        with open(read_file_path, 'r') as f:
            newLogFile = json.load(f)
            self.log_container[key]: dict[int, dict] = {'logs': dict(), 'schedules': dict()}

            for log in newLogFile['logs']:
                self.log_container[key]['logs'][str(log['time'])] = {'vehicles': log['vehicles'], 'tasks': log['tasks']}

            print(self.log_container[key]['logs']['1675263660000'])

    def get_log_by_timestamp(self, date: str, vnum: str, tnum: str, timestamp: str):
        key = self.getKey(date, vnum, tnum)
        if self.is_unloaded_date(key):
            self.readLog(date, vnum, tnum)
        print(type(timestamp))
        return self.log_container[key]['logs'][timestamp]

    def get_log_by_date(self, date: str, vnum: str, tnum: str):
        key = self.getKey(date, vnum, tnum)
        if self.is_unloaded_date(key):
            self.readLog(date, vnum, tnum)
        return self.log_container[key]
