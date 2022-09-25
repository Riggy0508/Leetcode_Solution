// https://leetcode.com/problems/kth-missing-positive-number

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        left,right=0,len(arr)-1
        
        while left<=right:
            mid=(left+right)//2
            if arr[mid]-mid-1<k:
                left+=1
            else:
                right-=1
        return left+k