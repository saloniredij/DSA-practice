class Solution:
    def tribonacci(self, n):
        dp = [float('-inf')] * (n+1)

        def tribo(num,dp):
            if num == 0:
                return num
            elif num == 1 or num == 2:
                return 1
            elif dp[num] != float('-inf'):
                return dp[num]
            else:
                dp[num] = tribo(num-1,dp) + tribo(num-2,dp) + tribo(num-3,dp)
                return dp[num]
        
        
        return tribo(n,dp)
                 