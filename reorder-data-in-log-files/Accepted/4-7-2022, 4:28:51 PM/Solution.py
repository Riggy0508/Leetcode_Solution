// https://leetcode.com/problems/reorder-data-in-log-files

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digits=[]
        letters=[]
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log.split())
        letters.sort(key=lambda x:x[0])
        letters.sort(key=lambda x:x[1:])
        
        for i in range(len(letters)):
            letters[i]=(" ").join(letters[i])
        letters.extend(digits)
        return letters