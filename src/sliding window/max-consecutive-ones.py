'''
Given a binary array nums and an integer k, return the maximum 
number of consecutive 1's in the array if you can flip at most k 0's.

 
Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]

Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]

Constraints:
1 <= nums.length <= 105
nums[i] is either 0 or 1.
0 <= k <= nums.length
'''


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        count = 0
        maxWindow = -1
        window = 0
        i,j=0,0
        while i <= j and j < len(nums):
            if nums[j] == 0:
                count+=1
            window+=1
            j+=1
            if count > k:
                i+=1
                window-=1
                if nums[i-1] == 0:
                    count-=1
            maxWindow = max(maxWindow,window)
        return maxWindow