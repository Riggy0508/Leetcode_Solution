// https://leetcode.com/problems/next-greater-element-i

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        hash1={}
        ans=[]

        for n2 in nums2:
            while stack and n2>stack[-1]:
                hash1[stack.pop()]=n2
            stack.append(n2)

        for n1 in nums1:
            if n1 in hash1:
                ans.append(hash1[n1])
            else:
                ans.append(-1)
        return ans