''' Given an array of integers arr, return true if the number of occurrences of each value 
in the array is unique or false otherwise.


Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true

Constraints:
1 <= arr.length <= 1000
-1000 <= arr[i] <= 1000 
'''


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hashmap = defaultdict(int)
        for i in arr:
            hashmap[i]+= 1
        
        seen = set()
        for key,val in hashmap.items():
            print(key,val)
            if val in seen:
                return False
            seen.add(val)
        return True