// https://leetcode.com/problems/defanging-an-ip-address

class Solution:
    def defangIPaddr(self, address: str) -> str:
        s=""
        
        for i in range(len(address)):
            if address[i]!=".":
                s+=(address[i])
            elif address[i]==".":
                s+=("[.]")
        return s
            
                    