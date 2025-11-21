class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [-1] * (n+1)

        def calc(i):
            # print(i,n)
            if i <= 1:
                return 0        
            if dp[i] != -1:
                return dp[i]
            dp[i] = min(calc(i-1) + cost[i-1],calc(i-2) + cost[i-2])
            # print(dp)
            return dp[i]
        # res = calc(n)
        return calc(n)
