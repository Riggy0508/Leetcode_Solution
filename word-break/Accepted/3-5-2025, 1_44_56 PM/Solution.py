// https://leetcode.com/problems/word-break

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word=set(wordDict)
        visited=set()
        q=deque([0])


        while q:
            start=q.popleft()

            if start in visited:
                continue
            visited.add(start)

            for end in range(start+1,len(s)+1):
                if s[start:end] in word:
                    if end==len(s):
                        return True

                    q.append(end)

        return False