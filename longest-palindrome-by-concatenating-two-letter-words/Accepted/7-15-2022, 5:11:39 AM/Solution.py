// https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        res,looking=0,defaultdict(int)
        for word in words:
            if looking[word]:
                looking[word]-=1
                res+=4
                continue
            looking[word[1]+word[0]]+=1
        #print(looking[word[1]+word[0]]) ---- smart move
            
        for i in looking:
            if i[0]==i[1] and looking[i]:
                res+=2
                break
                
        return res