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