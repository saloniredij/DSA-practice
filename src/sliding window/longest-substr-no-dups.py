'''
Longest Substring Without Repeating Characters
Given a string s, find the length of the longest substring without duplicate characters.

Example 1:
Input: s = "zxyzxyz"
Output: 3

Example 2:
Input: s = "xxxx"
Output: 1

Constraints:
0 <= s.length <= 10^3
s may consist of printable ASCII characters.


'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        i,j = 0,0
        maxLen = 0
        while j < len(s):
            if s[j] not in seen:
                seen.add(s[j])
                maxLen = max(maxLen, j-i+1)
                j+=1
            else:
                i+=1
                seen.remove(s[i-1])
            
            # print(seen)
            # print(maxLen)
        return maxLen