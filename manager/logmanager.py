import json
import os
import sys


class LogManager:

    UNIT_TIME = 60000

    def __init__(self):
        self.log_container: dict[str, dict] = dict()

    def is_unloaded_date(self, date: str) -> bool:
        """
        if already read log at date, return false

        Args:
            date (str): yyyymmdd
        """
        return not date in self.log_container

    def getKey(self, date: str, vnum: str, tnum: str) -> str:
        """
        generate Key value with data, vnum, tnum

        Args:
            date (str): yyyymmdd
            vnum (str): vehicle number
            tnum (str): task number
        Returns:
            str: key string
        """
        return f"{date}{vnum}{tnum}"

    def readLog(self, date: str, vnum: str, tnum: str) -> bool:
        """
        read log data

        Args:
            date (str): yyyymmdd
            vnum (str): vehicle number
            tnum (str): task number
        return:
            bool : Read pass/fail
        """

        key = self.getKey(date, vnum, tnum)
        if not self.is_unloaded_date(key):
            return True

        read_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'log')
        read_file_name = f'{date}_{vnum}_{tnum}.json'
        if not read_file_name in os.listdir(read_file_path):
            return False

        with open(read_file_path + "/" + read_file_name, 'r') as f:
            newLogFile = json.load(f)
            self.log_container[key]: dict[int, dict] = {'logs': dict(), 'schedules': dict(), 'prev_schedules': []}

        for log in newLogFile['logs']:
            self.log_container[key]['logs'][log['time']] = log

        for schedule in newLogFile['schedules']:
            self.log_container[key]['schedules'][schedule['time']] = schedule

        self.log_container[key]['prev_schedules'] = newLogFile['prev_schedules']

    def get_log_by_timestamp(self, date: str, vnum: str, tnum: str, timestamp: int) -> dict:
        """
        get log info by timestamp ~ timestamp + delta

        Args:
            date (str): yyyymmdd
            vnum (str): vehicle num
            tnum (str): task num
            timestamp (int): timestamp

        Returns:
            dict: log data untill timestamp to timestamp
        """
        key = self.getKey(date, vnum, tnum)

        if self.is_unloaded_date(key):
            flag = self.readLog(date, vnum, tnum)
            if flag == False:
                return {}
        return self.log_container[key]['logs'][timestamp]

    def get_log_by_timestamp_delta(self, date: str, vnum: str, tnum: str, timestamp: int, delta: int) -> dict:
        """
        get log info by timestamp ~ timestamp + delta

        Args:
            date (str): yyyymmdd
            vnum (str): vehicle num
            tnum (str): task num
            timestamp (int): timestamp
            delta (int): minute

        Returns:
            dict: log data untill timestamp to timestamp + delta
        """

        key = self.getKey(date, vnum, tnum)

        if self.is_unloaded_date(key):
            flag = self.readLog(date, vnum, tnum)
            if flag == False:
                return {}

        result = []
        for i in range(0, delta):
            cur_timestamp = timestamp + (i * self.UNIT_TIME)
            if cur_timestamp in self.log_container[key]['logs']:
                result.append(self.log_container[key]['logs'][cur_timestamp])
            else:
                print("timestamp key error")

        return result

    def get_log_by_date(self, date: str, vnum: str, tnum: str) -> dict:
        """
        get full log at date

        Args:
            date (str): yyyymmdd
            vnum (str): vehicle num
            tnum (str): task num

        Returns:
            dict: all log data
        """

        key = self.getKey(date, vnum, tnum)

        if self.is_unloaded_date(key):
            flag = self.readLog(date, vnum, tnum)
            if flag == False:
                return {}

        return self.log_container[key]

    def get_schedule_by_timestamp(self, date: str, vnum: str, tnum: str, timestamp: int):

        return None
