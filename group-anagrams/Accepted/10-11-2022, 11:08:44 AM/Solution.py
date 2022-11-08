// https://leetcode.com/problems/group-anagrams

# Because we wanna return list of list and we are gonna using the concept of hashing over here. Let's start with defining our hashmap with a default list 
# Late on, we are gonna traverse the independant word from the list and then it's indepened character. 
#Once that is done we are maintaining the count of each char of a string and then appending it onto the res list. After the loop's we will have a group of string's with the same hash value and we can return.
#We are using tuple here because we don't wanna have any duplicate's plus there are mulitple objects that we are dealing with. 

#Reference : https://www.w3schools.com/python/python_tuples.asp


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)
        
        for string in strs:
            count=[0]*26
            for char in string:
                count[ord(char)-ord("a")]+=1
            res[tuple(count)].append(string)
        return res.values()
        
        