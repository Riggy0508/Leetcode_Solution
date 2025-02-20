// https://leetcode.com/problems/custom-sort-string

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        result=[]
#We are gonna keep a count of all the characters in string S so that we know how many characters we are working with
        char_Count=Counter(s)
#Once done with that we will traverse the ORDER string
        for char in order:
            #Checking if the character in order sequence is present in S string and if it's present add it into the result and also making sure that all the charactesr are present
            if char in char_Count:
                result.append(char*char_Count[char])
#Once we are done with adding all the characters we are gonna delete it as it will make it easier to check what all charactesr are now missing and then we can add them in the result
            del char_Count[char]

#If there are any more characters that are missing then we will simply add them in the list
        for char,count in char_Count.items():
            result.append(char*count)
#Since we need to return a string we will 
        return "".join(result)