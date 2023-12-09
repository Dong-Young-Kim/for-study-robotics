class MovAvgFilter:
    def __init__(self, window_size):
        self.window_size = window_size
        self.buffer = []

    def update(self, value):
        self.buffer.append(value)
        if len(self.buffer) > self.window_size:
            self.buffer.pop(0)

    def get_average(self):
        if len(self.buffer) == 0:
            return None
        return sum(self.buffer) / len(self.buffer)
