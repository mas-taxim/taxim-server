import json
import os
import sys


class LogManager:

    UNIT_TIME = 60000

    def __init__(self):
        self.log_container: dict[str, dict] = dict()

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

        read_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'log')
        read_file_name = f'{date}_{vnum}_{tnum}.json'
        if not read_file_name in os.listdir(read_file_path):
            return False

        key = self.getKey(date, vnum, tnum)

        with open(read_file_path + "/" + read_file_name, 'r') as f:
            newLogFile = json.load(f)
            self.log_container[key]: dict[int, dict] = {'logs': dict(), 'schedules': dict(), 'prev_schedules': []}

        # log dict that key is timestamp
        for log in newLogFile['logs']:
            self.log_container[key]['logs'][log['time']] = log

        # schedule dict that key is timestamp
        for schedule in newLogFile['schedules']:
            self.log_container[key]['schedules'][schedule['time']] = schedule

        self.log_container[key]['prev_schedules'] = newLogFile['prev_schedules']

        return True

    def is_data_loaded(self, date: str, vnum: str, tnum: str) -> bool:
        """
        if already read log at date, return false

        Args:
            date (str): yyyymmdd
        """

        if self.getKey(date, vnum, tnum) in self.log_container:
            return True

        return self.readLog(date, vnum, tnum)

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

        if self.is_data_loaded(date, vnum, tnum) == False:
            return {}

        return self.log_container[self.getKey(date, vnum, tnum)]

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
        if self.is_data_loaded(date, vnum, tnum) == False:
            return {}

        return self.log_container[self.getKey(date, vnum, tnum)]['logs'].get(timestamp)

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

        if self.is_data_loaded(date, vnum, tnum) == False:
            return []

        result = []
        for i in range(0, delta):
            cur_timestamp = timestamp + (i * self.UNIT_TIME)
            cur_logs = self.get_log_by_timestamp(date, vnum, tnum, cur_timestamp)
            if cur_logs == None:
                break
            result.append(cur_logs)

        return result

    def get_schedule_by_timestamp(self, date: str, vnum: str, tnum: str, timestamp: int) -> dict:

        if self.is_data_loaded(date, vnum, tnum) == False:
            return {}

        key = self.getKey(date, vnum, tnum)
        result = self.log_container[key]['schedules'].get(timestamp)
        if result == None:
            return None

        for i in range(0, len(result['logs'])):
            prev_schedules = result['logs'][i]['prev_schedules']
            if len(prev_schedules) == 0:
                continue

            schedules = []
            for j in prev_schedules:
                schedules.append(self.log_container[key]['prev_schedules'][j])

            result['logs'][i]['schedules'] = schedules + result['logs'][i]['schedules']

        return result

    def get_schedule_by_timestamp_delta(self, date: str, vnum: str, tnum: str, timestamp: int, delta: int) -> list:

        if self.is_data_loaded(date, vnum, tnum) == False:
            return []

        result = []
        for i in range(0, delta):
            cur_timestamp = timestamp + (i * self.UNIT_TIME)
            cur_schedule = self.get_schedule_by_timestamp(date, vnum, tnum, cur_timestamp)
            if cur_schedule == None:
                break
            result.append(cur_schedule)

        return result
