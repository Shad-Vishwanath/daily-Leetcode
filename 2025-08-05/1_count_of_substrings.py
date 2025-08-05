"""
🧠 Problem: Count of Substrings Containing Every Vowel and K Consonants II  
🔗 Link: https://leetcode.com/problems/count-of-substrings-containing-every-vowel-and-k-consonants-ii  

💡 Approach:
   - Use a **sliding window** to dynamically scan through the string.
   - Maintain two dictionaries:
     - One for tracking required vowels (`'a', 'e', 'i', 'o', 'u'`)
     - One for tracking how many vowels are currently in the window.
   - For each character:
     - If it's a vowel, update vowel count and unique vowel tracker.
     - If it's a consonant, increment a `currentK` counter.
   - Shrink the window from the left when `currentK > k`.
   - When the window has **all 5 vowels** and exactly **k consonants**, start counting:
     - Also account for **extra vowels at the start** of the window that don't affect the condition — each of these creates a new valid substring.

📌 Core idea: Track valid substrings by ensuring every vowel is present **once**, and exactly **k consonants** exist in the window. Use `extraLeft` to count overlapping valid substrings.

⏱️ Time Complexity: O(n) — each character is visited at most twice  
📦 Space Complexity: O(1) — fixed dictionary size
"""

class Solution(object):
    def countOfSubstrings(self, word, k):
        frequencies = [{}, {}]
        for v in "aeiou":
            frequencies[0][v] = 1
        
        response, currentK, vowels, extraLeft, left = 0, 0, 0, 0, 0
        for right, rightChar in enumerate(word):
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
