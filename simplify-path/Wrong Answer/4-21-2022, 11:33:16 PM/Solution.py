// https://leetcode.com/problems/simplify-path

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        cur=""
        
        for p in path+"/":
            if p=="/":
                if cur=="..":
                    if stack:
                        stack.pop()
                elif cur!="" and cur!=".":
                    stack.append(cur)
                    cur=""
            else:
                cur+=p
                
        return "/"+"/".join(stack)
        """
        stack=[]
        cur=""
        for p in path +"/":
            #print(p)
            if p=="/":
                #print(cur)
                if cur=="..":
                    if stack:
                        stack.pop()
                elif cur!="" and cur!=".":
                    stack.append(cur)
                cur=""
            else: 
                cur+=p
                    
        return "/"+"/".join(stack)
           """ 