// https://leetcode.com/problems/kids-with-the-greatest-number-of-candies

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        maxCandies=max(candies)

        answer=[]

        for i in range(len(candies)):
            if candies[i]+extraCandies>=maxCandies:
                answer.append(True)
            else:
                answer.append(False)

        return answer