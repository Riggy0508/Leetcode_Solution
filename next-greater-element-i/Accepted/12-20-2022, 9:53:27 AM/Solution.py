// https://leetcode.com/problems/next-greater-element-i

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        #Creating a hashmap to generate key value pair
        nums1h={val:i for i,val in enumerate(nums1)}
        print(nums1h)
        res=[-1]*len(nums1)

        stack=[]

        for i in range(len(nums2)):
            cur=nums2[i]

            while stack and cur>stack[-1]:
                val=stack.pop()
                idx=nums1h[val]
                res[idx]=cur
            if cur in nums1h:
                stack.append(cur)
        return res
