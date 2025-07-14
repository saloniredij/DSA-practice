'''
You are given an integer array nums and an integer k.
In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.
Return the maximum number of operations you can perform on the array.

 

Example 1:
Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.

Constraints:
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^9
1 <= k <= 10^9

'''




class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        ops = 0
        numsCount = Counter(nums)
        for num,counts in numsCount.items():
            val2 = k - num
            print(val2)

            if num < val2 or val2 not in numsCount:
                continue
            
            if num == val2:
                ops += counts//2
            else:
                ops+= min(counts,numsCount[val2])
        return ops
            

        # nums = sorted(nums)
        # i,j = 0,len(nums)-1
        # ops = 0
        # while i < j:
        #     tempAdd = nums[i] + nums[j]
        #     if tempAdd == k:
        #         ops+=1
        #         i+=1
        #         j-=1
        #     elif tempAdd > k:
        #         j-=1
        #     else:
        #         i+=1
        # return ops
            

        