// https://leetcode.com/problems/longest-repeating-character-replacement

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        all_letters=set(s)
        res=0

        for letter in all_letters:
            start=0
            count=0
            
            for end in range(len(s)):
                if s[end]==letter:
                    count+=1

                while not self.is_valid(start,end,count,k):
                    if s[start]==letter:
                        count-=1
                    start+=1


                res=max(res,end+1-start)

        return res

    def is_valid(self,start,end,count,k):
        return end-start+1-count<=k
