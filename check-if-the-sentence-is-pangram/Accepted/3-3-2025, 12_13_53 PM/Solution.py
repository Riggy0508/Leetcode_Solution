// https://leetcode.com/problems/check-if-the-sentence-is-pangram

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        count=set(sentence)

        for ch in sentence:
            if ch in count:
                continue
            else:
                return False

        return len(count)==26
