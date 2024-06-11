import time

class Timer:
    def __init__(self, duration):
        self.duration = duration
        self.remaining_time = duration
        self.is_running = False

    def start(self):
        self.start_time = time.time()
        self.is_running = True

    def stop(self):
        if self.is_running:
            self.remaining_time -= time.time() - self.start_time
            self.is_running = False

    def reset(self):
        self.remaining_time = self.duration
        self.is_running = False

    def get_remaining_time(self):
        if self.is_running:
            elapsed_time = time.time() - self.start_time
            self.remaining_time = max(0, self.remaining_time - elapsed_time)
        return self.remaining_time

    def is_finished(self):
        return self.get_remaining_time() <= 0
