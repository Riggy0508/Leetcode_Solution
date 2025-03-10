// https://leetcode.com/problems/kth-missing-positive-number

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        missingCount=index=0
        current=1

        while missingCount<k:
            if index<len(arr) and arr[index]==current:
                index+=1
            else:
                missingCount+=1
                if missingCount==k:
                    return current

            current+=1
        
        return -1