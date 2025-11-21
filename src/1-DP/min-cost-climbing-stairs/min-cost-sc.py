class Solution:
    def minCostClimbingStairs(self, cost: List[int]):
        n = len(cost)
        prev = 0            #1
        prev2 = 0           #0

        for i in range(2,n+1):
            curr = min(prev + cost[i-1], prev2 + cost[i-2])
            prev2,prev = prev, curr
        
        # print(curr,prev,prev2)
        return curr
       
