"""
🧠 Problem: Fruit Into Baskets II
🔗 Link: https://leetcode.com/problems/fruit-into-baskets-ii
💡 Approach:
   - Each fruit has a size, and each basket can hold **at most one fruit** that is less than or equal to its capacity.
   - For each fruit in the list:
     - Iterate through the baskets to find the first one that can hold it (i.e., basket capacity >= fruit size).
     - If a valid basket is found, mark that basket as used (set to 0).
     - If not, count the fruit as "unplaced".
   - Return the total number of fruits that could **not** be placed in any basket.

📌 This is a **greedy matching** problem — matching each fruit to the first available compatible basket.

⏱️ Time Complexity: O(m * n)  
   (where `m` is the number of fruits and `n` is the number of baskets)

📦 Space Complexity: O(1)
"""

class Solution(object):
    def numOfUnplacedFruits(self, fruits, baskets):
        count = 0
        n = len(baskets)
        for fruit in fruits:
            unset = 1
            for i in range(n):
                if fruit <= baskets[i]:
                    baskets[i] = 0  # Mark basket as used
                    unset = 0
                    break
            count += unset
        return count
