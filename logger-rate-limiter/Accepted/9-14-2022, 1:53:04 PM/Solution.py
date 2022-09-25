// https://leetcode.com/problems/logger-rate-limiter

class Logger:

    def __init__(self):
        self.message_dict={}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.message_dict:
            self.message_dict[message]=timestamp
            return True
        if timestamp-self.message_dict[message]>=10:
            self.message_dict[message]=timestamp
            return True
        else:
            return False
        
# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)