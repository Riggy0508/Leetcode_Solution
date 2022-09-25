// https://leetcode.com/problems/reveal-cards-in-increasing-order

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n=len(deck)
        index=collections.deque(range(n))
        ans=[None]*n
        
        print(index)
        for card in sorted(deck):
            ans[index.popleft()]=card
            if index:
                index.append(index.popleft())
        
        return ans
                