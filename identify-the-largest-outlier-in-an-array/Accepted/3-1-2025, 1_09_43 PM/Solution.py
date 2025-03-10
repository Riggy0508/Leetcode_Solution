// https://leetcode.com/problems/identify-the-largest-outlier-in-an-array

class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:

        total=sum(nums)
        
        hash1=defaultdict(int)

        for num in nums:
            if num in hash1:
                hash1[num]+=1
            else:
                hash1[num]=1


        largest=float("-inf")


        for num in hash1.keys():

            potential_outlier=total-2*num

            if potential_outlier in hash1:
                if potential_outlier!=num or hash1[num]>1:
                    largest=max(largest,potential_outlier)


        return largest

