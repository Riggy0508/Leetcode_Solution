// https://leetcode.com/problems/unique-email-addresses

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        count=len(emails)
        for e in emails:
            e=e.split('@')
            if e[1]!='leetcode.com':
                count-=1
        return count
        