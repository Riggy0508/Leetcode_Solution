// https://leetcode.com/problems/sequential-digits

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        sample="123456789"
        n=10
        nums=[]


        for length in range(len(str(low)),len(str(high))+1):
            for i in range(n-length):
                num=int(sample[i:i+length])
                if num>=low and num<=high:
                    nums.append(num)

        return nums