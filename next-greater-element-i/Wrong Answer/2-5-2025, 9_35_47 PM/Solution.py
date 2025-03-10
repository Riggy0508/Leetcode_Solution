// https://leetcode.com/problems/next-greater-element-i

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        hash1={}
        result=[]

        for num in nums2:
            if stack and stack[-1]<num:
                hash1[stack.pop()]=num
            stack.append(num)

        for num in nums1:
            if num in hash1:
                result.append(hash1[num])
            else:
                result.append(-1)

        return result