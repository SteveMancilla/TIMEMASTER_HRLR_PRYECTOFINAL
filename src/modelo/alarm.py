from datetime import datetime, timedelta
import time

class Alarm:
    def __init__(self, alarm_time):
        self.alarm_time = datetime.strptime(alarm_time, "%H:%M")
        self.is_set = False

    def set(self):
        now = datetime.now()
        alarm_time_today = now.replace(hour=self.alarm_time.hour, minute=self.alarm_time.minute, second=0, microsecond=0)
        if alarm_time_today < now:
            alarm_time_today += timedelta(days=1)
        self.time_to_wait = (alarm_time_today - now).total_seconds()
        self.start_time = time.time()
        self.is_set = True

    def check(self):
        if not self.is_set:
            return False
        return time.time() >= self.start_time + self.time_to_wait

    def reset(self):
        self.is_set = False
