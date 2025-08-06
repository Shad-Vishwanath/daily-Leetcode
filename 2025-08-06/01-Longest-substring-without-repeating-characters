"""🔗 LeetCode Link: Longest Substring Without Repeating Characters

🧠 Problem Summary:
Given a string s, return the length of the longest substring without repeating characters.

✅ Solution Status:
✔️ Accepted – All 988 test cases passed
🚀 Runtime: 15 ms (Beats 90.59% of Python submissions)
💾 Memory: 13.32 MB (Beats 16.81%)

💡 Approach:
-> Used an array charIndex of size 128 (ASCII range) to store last seen indices of characters.

-> Utilized the sliding window technique to maintain a valid substring without repeating characters.

-> Updated the left pointer only when a duplicate character was found within the current window.

-> Tracked the maximum window size in maxLength.

🧮 Time & Space Complexity:
Time Complexity: O(n)

Space Complexity: O(1) – fixed-size array for ASCII characters
"""
Program :
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        n = len(s)
        maxLength = 0
        charIndex = [-1]*128
        left =0

        for right in range(n):
            if charIndex[ord(s[right])] >= left:
                left = charIndex[ord(s[right])] + 1
            charIndex[ord(s[right])] = right
            maxLength = max(maxLength, right - left +1)

        return maxLength
