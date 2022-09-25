// https://leetcode.com/problems/unique-email-addresses

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique=set()
        
        for email in emails:
            name,domain=email.split('@')
            
            l=name.split('+')[0].replace('.','')
            
            unique.add(l+'@'+domain)
        return len(unique)
        