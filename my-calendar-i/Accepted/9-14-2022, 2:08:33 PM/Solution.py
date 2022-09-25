// https://leetcode.com/problems/my-calendar-i

class MyCalendar:

    def __init__(self):
        self.calendar=[]

    def book(self, start: int, end: int) -> bool:
        for s,e in self.calendar:
            if s<end and start<e:
                return False
        self.calendar.append((start,end))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)