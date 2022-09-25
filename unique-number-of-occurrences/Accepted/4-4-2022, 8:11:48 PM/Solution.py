// https://leetcode.com/problems/unique-number-of-occurrences

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hashMap={}
        for i in range(len(arr)):
            if arr[i] in hashMap:
                hashMap[arr[i]]+=1
            else:
                hashMap[arr[i]]=1
        
        hashMap1={}
        for key,val in hashMap.items():
            if val in hashMap1.keys():
                return False
            else:
                hashMap1[val]=key
        return True
            