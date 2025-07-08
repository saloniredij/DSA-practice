'''
Determine if Two Strings Are Close

Two strings are considered close if you can attain one from the other using the following operations:

Operation 1: Swap any two existing characters.
For example, abcde -> aecdb
Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
You can use the operations on either string as many times as necessary.

Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.
ex 1
Input: word1 = "abc", word2 = "bca"
Output: true
Explanation: You can attain word2 from word1 in 2 operations.
Apply Operation 1: "abc" -> "acb"
Apply Operation 1: "acb" -> "bca"

ex 2
Input: word1 = "a", word2 = "aa"
Output: false
Explanation: It is impossible to attain word2 from word1, or vice versa, in any number of operations.

Example 3:
Input: word1 = "cabbba", word2 = "abbccc"
Output: true
Explanation: You can attain word2 from word1 in 3 operations.
Apply Operation 1: "cabbba" -> "caabbb"
Apply Operation 2: "caabbb" -> "baaccc"
Apply Operation 2: "baaccc" -> "abbccc"

1 <= word1.length, word2.length <= 10^5

'''

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1)!= len(word2):
            return False

        word1Count = Counter(word1)
        word2Count = Counter(word2)
        a = word1Count.keys() == word2Count.keys()
        b = sorted(list(word1Count.values())) == sorted(list(word2Count.values()))
        # print(a,b)
        return True if (a and b) else False



                
        # hashmap = defaultdict()
        # count1, count2 = [0]*26,[0]*26
        # for i in range(len(word1)):
        #     x = abs(ord('a') - ord(word1[i]))
        #     count1[x] = 1
        #     y = abs(ord('a') - ord(word2[i]))
        #     count2[y] = 1
