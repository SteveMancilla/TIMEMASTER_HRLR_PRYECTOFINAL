import time

class Pomodoro:
    def __init__(self, work_time, break_time):
        self.work_time = work_time * 60
        self.break_time = break_time * 60
        self.remaining_time = self.work_time
        self.is_running = False
        self.is_break = False

    def start(self):
        self.start_time = time.time()
        self.is_running = True

    def stop(self):
        if self.is_running:
            self.remaining_time -= time.time() - self.start_time
            self.is_running = False

    def reset(self):
        self.remaining_time = self.work_time if not self.is_break else self.break_time
        self.is_running = False

    def get_remaining_time(self):
        if self.is_running:
            elapsed_time = time.time() - self.start_time
            self.remaining_time = max(0, self.remaining_time - elapsed_time)
        return self.remaining_time

    def is_finished(self):
        return self.get_remaining_time() <= 0

    def switch(self):
        if self.is_finished():
            self.is_break = not self.is_break
            self.reset()
