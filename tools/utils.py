
import time


class Accumulator:
    def __init__(self, *args, **kwargs):
        self.total = 0
        self.quantity = 0

    def add_value(self, value):
        self.total = self.total + value
        self.quantity = self.quantity + 1

    def mean(self):
        if self.quantity == 0:
            return 0
        return self.total/self.quantity

    def __str__(self):
        return "total is {0}, quantity is {1},mean is {2}".format(self.total, self.quantity, self.mean())


class StopWatch:
    def __init__(self, *args, **kwargs):
        self.start_time = time.process_time()

    def elapse_time(self):
         return time.process_time()  - self.start_time

    def __str__(self):
        return "elapse {0}".format(self.elapse_time())
