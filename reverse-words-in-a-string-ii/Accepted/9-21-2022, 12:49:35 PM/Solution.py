// https://leetcode.com/problems/reverse-words-in-a-string-ii

class Solution:
    def reverse(self,s:list,left:int,right:int)->None:
        #in this function we are reverse every string that we get.
        
        #by using two pointer method we are gonna reverse the string
        while left<right:
            s[left],s[right]=s[right],s[left]
            left+=1
            right-=1
    
    def reverse_each_word(self,s:list)->None:
        #we are trying to reverse every single indepent word
        n=len(s)
        start=0
        end=0
        #we are finding the first " "(empty string) and then we are reversing it. 
        while start<n:
            while end<n and s[end]!=" ":
                end+=1
            self.reverse(s,start,end-1)
            start=end+1
            end+=1

    def reverseWords(self, s: List[str]) -> None:
        #first we are gonna reverse the string and then reverse the independ word later on
        """
        Do not return anything, modify s in-place instead.
        """
        self.reverse(s,0,len(s)-1)
        
        self.reverse_each_word(s)