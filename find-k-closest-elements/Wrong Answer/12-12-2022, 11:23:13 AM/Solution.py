// https://leetcode.com/problems/find-k-closest-elements

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l,r=0,len(arr)-k

        while l<r:
            m=(l+r)//2
            if x-arr[m]>arr[k-m]:
                l=m+1
            else:
                r=m
        return arr[l:l+k]