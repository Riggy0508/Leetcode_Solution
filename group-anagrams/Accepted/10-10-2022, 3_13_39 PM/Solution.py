// https://leetcode.com/problems/group-anagrams

# Because we wanna return list of list and we are gonna using the concept of hashing over here. Let's start with defining our hashmap with a default list 
# Late on, we are gonna traverse the independant word from the list and then it's indepened character. 


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)
        
        for string in strs:
            count=[0]*26
            for char in string:
                count[ord(char)-ord("a")]+=1
            res[tuple(count)].append(string)
        return res.values()
        
        