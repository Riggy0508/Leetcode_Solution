// https://leetcode.com/problems/buddy-strings

class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        c1,c2=Counter(s),Counter(goal)
        if c1!=c2:
            return False
        diff=sum([1 for i in range(len(s)) if s[i]!=goal[i]])
        if diff==2:
            return True
        elif diff==0:
            return any([cnt>1 for char,cnt in c1.items()])
        else:
            return False
                
            