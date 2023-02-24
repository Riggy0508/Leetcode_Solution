// https://leetcode.com/problems/remove-invalid-parentheses

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        res=[]
        q=collections.deque([])

        if not s or len(s)==0:
            return res

        seen=set()
        flag=False

        q.append(s)
        seen.add(s)

        while q and not flag:
            qLen=len(q)
            for i in range(qLen):
                curr=q.popleft()
                #print(curr)
                if self.isValid(curr):
                    flag=True
                    res.append(curr)
                else:
                    if not flag:
                        #print(curr)
                        for j in range(len(curr)):
                            child=curr[0:j]+curr[j+1:]
                            #print(child)
                            if child not in seen:
                                q.append(child)
                                seen.add(child)
        return res

    def isValid(self,s):
        count=0

        for k in range(len(s)):
            if s[k]=="(":
                count+=1
            else:
                if s[k]==")":
                    if count==0:
                        return False
                    count-=1
        return count==0
