// https://leetcode.com/problems/find-players-with-zero-or-one-losses

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        zeroLoss,oneLoss,moreLoss=set(),set(),set()

        for match in matches:
            winner,loser=match[0],match[1]

            if winner not in oneLoss and winner not in moreLoss:
                zeroLoss.add(winner)

            if loser in zeroLoss:
                zeroLoss.remove(loser)
                oneLoss.add(loser)
                
            elif loser in oneLoss:
                oneLoss.remove(loser)
                moreLoss.add(loser)

            elif loser in moreLoss:
                continue
            else:
                oneLoss.add(loser)

        ans=[sorted(list(zeroLoss)),sorted(list(oneLoss))]
        return ans