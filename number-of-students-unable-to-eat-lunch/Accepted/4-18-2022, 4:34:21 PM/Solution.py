// https://leetcode.com/problems/number-of-students-unable-to-eat-lunch

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count=0
        
        while True:
            k=len(students)
            if k==0:break
    
            if students[0]==sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                count=0
            elif students[0]!=sandwiches[0]:
                students.append(students[0])
                students.pop(0)
                count+=1
            if count==k:
                break
        return count