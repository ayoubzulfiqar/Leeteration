class Logger:

    def __init__(self):
        self.message_timestamps = {}
        self.RATE_LIMIT_SECONDS = 10

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.message_timestamps:
            self.message_timestamps[message] = timestamp
            return True
        else:
            last_printed_timestamp = self.message_timestamps[message]
            if timestamp - last_printed_timestamp >= self.RATE_LIMIT_SECONDS:
                self.message_timestamps[message] = timestamp
                return True
            else:
                return False

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)