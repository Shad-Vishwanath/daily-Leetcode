"""
🧠 Problem: Count of Substrings Containing Every Vowel and K Consonants II
🔗 Link: https://leetcode.com/problems/count-of-substrings-containing-every-vowel-and-k-consonants-ii
💡 Approach:
   - Use a sliding window to maintain the substring window.
   - Count vowels and consonants within the window.
   - Track substrings that contain all vowels at least once and exactly K consonants.
   - Efficient tracking of vowel frequency using a dictionary or counter.

⏱️ Time Complexity: O(n)
📦 Space Complexity: O(1) — constant extra space for tracking vowels and consonants
"""


class Solution(object):
    def countOfSubstrings(self, word, k):
        frequencies = [{},{}]
        for v in "aeiou":
            frequencies[0][v] = 1
        
        response, currentK, vowels, extraLeft, left = 0,0,0,0,0
        for right,rightChar in enumerate(word):
            if rightChar in frequencies[0]:
                frequencies[1][rightChar] = frequencies[1].get(rightChar, 0) + 1
                if frequencies[1][rightChar] == 1:
                    vowels += 1
            else:
                currentK += 1

            while currentK > k:
                leftChar = word[left]
                if leftChar in frequencies[0]:
                    frequencies[1][leftChar] -= 1
                    if frequencies[1][leftChar] == 0:
                        vowels -= 1
                else:
                    currentK -= 1
                left += 1
                extraLeft = 0

            while vowels == 5 and currentK == k and left < right and word[left] in frequencies[0] and frequencies[1][word[left]] > 1:
                extraLeft += 1
                frequencies[1][word[left]] -= 1
                left += 1

            if currentK == k and vowels == 5:
                response += (1 + extraLeft)

        return response

        
