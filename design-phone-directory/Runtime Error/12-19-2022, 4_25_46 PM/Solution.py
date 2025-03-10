// https://leetcode.com/problems/design-phone-directory

class PhoneDirectory:

    def __init__(self, maxNumbers: int):

        self.numbers={i for i in range(maxNumbers)}
        #print(self.numbers)

    def get(self) -> int:
        if self.numbers is None:
            return -1
        else:
            return self.numbers.pop()
        

    def check(self, number: int) -> bool:
        if number in self.numbers:
            return True
        else:
            return False

    def release(self, number: int) -> None:
        self.numbers.add(number)
        


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)