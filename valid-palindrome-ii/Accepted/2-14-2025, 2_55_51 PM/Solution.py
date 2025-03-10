// https://leetcode.com/problems/valid-palindrome-ii

class Solution:
    def validPalindrome(self, nums: str) -> bool:
        l,r=0,len(nums)-1

        while l<r:
            if nums[l]!=nums[r]:
                if self.check(nums,l+1,r) or self.check(nums,l,r-1):
                    return True
                else:
                    return False

            l+=1
            r-=1

        return True



    def check(self,nums,l,r):

        while l<r:
            if nums[l]!=nums[r]:
                return False

            l+=1
            r-=1

        return True
