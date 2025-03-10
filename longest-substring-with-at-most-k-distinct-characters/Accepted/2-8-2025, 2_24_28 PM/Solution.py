// https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k==0:
            return 0

        max_length=0
        left=0
        countMap=defaultdict(int)

        for right in range(len(s)):
            countMap[s[right]]+=1

            while len(countMap)>k:
                countMap[s[left]]-=1

                if countMap[s[left]]==0:
                    del countMap[s[left]]
                left+=1
            
            max_length=max(max_length,right-left+1)

        return max_length