import time


class Analytics(object):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Analytics, cls).__new__(cls)
            cls.queries = 0
            cls.started = time.time()
        return cls._instance

    def inc_counter(self):
        self.queries += 1

    def get_uptime(self):
        return int(time.time() - self.started)


