// https://leetcode.com/problems/check-if-the-sentence-is-pangram

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        hash1={}

        for s in sentence:
            if s not in hash1:
                hash1[s]=1
            else:
                hash1[s]+=1

        return len(hash1)==26