// https://leetcode.com/problems/kth-missing-positive-number

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        missing=0
        expected=1
        index=0

        while missing<k:
            if index<len(arr) and arr[index]==expected:
                index+=1
            else:
                missing+=1
            
            if missing==k:
                return expected
            expected+=1
        
