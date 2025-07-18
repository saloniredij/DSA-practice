'''
Given a string s and an integer k, return the maximum number of 
vowel letters in any substring of s with length k.

Example:
Input: s = "abciiidef", k = 3
Output: 3
substring "iii"

Constraints:

1 <= s.length <= 105
1 <= k <= s.length
'''

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        i=0
        maxVowels = 0
        while i < k:
            if s[i] in ('aeiou'):
                maxVowels+=1
            i+=1
        j=k
        i = 1
        count = maxVowels
        while j < len(s):
            if s[i-1] in ('aeiou'):
                count-=1
            if s[j] in ('aeiou'):
                count+=1
            maxVowels = max(maxVowels,count)
            i+=1
            j+=1
        return maxVowels