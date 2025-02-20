// https://leetcode.com/problems/intersection-of-two-arrays

class Solution:
    def intersection1(setlf,set1,set2):
            return [x for x in set1 if x in set2]
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        set1=set(nums1)
        set2=set(nums2)

        if len(set1)<len(set2):
            return self.intersection1(set1,set2)
        else:
            return self.intersection1(set2,set1)