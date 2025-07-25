'''
given an integer array nums consisting of n elements, and an integer k.
Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

 

Example 1:
Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000

Example 2:
Input: nums = [5], k = 1
Output: 5.00000
 
Constraints:

n == nums.length
1 <= k <= n <= 10^5
-10^4 <= nums[i] <= 10^4
'''




class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        avg = 0
        for i in range(k):
            avg += nums[i]
        avg = avg/k
        maxAvg = avg
        i = 1
        j = i + k - 1
        while j < len(nums):
            temp = (avg * k) - nums[i-1]
            temp += nums[j]
            avg = temp/k
            maxAvg = max(maxAvg,avg)
            i+=1
            j = i + k - 1
        # print(maxAvg)
        return maxAvg
