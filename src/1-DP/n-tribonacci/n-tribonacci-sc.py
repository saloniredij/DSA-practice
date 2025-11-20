class Solution:
    def tribonacci(self, n):
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1

        prev = 1                        #2
        prev2 = 1                       #1
        prev3 = 0                       #0

        for i in range(3,n+1):
            curr = prev + prev2 + prev3

            prev3, prev2,prev = prev2, prev, curr

        return curr