✅ Problem 2: Fruit Into Baskets
🔹 Approach: Sliding Window with HashMap (defaultdict)
🔹 Key Idea: Maintain a window of at most 2 fruit types
🔹 Time Complexity: O(N)
🔹 Status: Accepted
🔹 Runtime: 219 ms (🥉 Beats ~53%)
🔹 Memory: 16.75 MB

python
Copy
Edit
from collections import defaultdict

class Solution:
    def totalFruit(self, fruits):
        start = 0
        max_len = 0
        fruit_count = defaultdict(int)

        for end in range(len(fruits)):
            fruit_count[fruits[end]] += 1

            while len(fruit_count) > 2:
                fruit_count[fruits[start]] -= 1
                if fruit_count[fruits[start]] == 0:
                    del fruit_count[fruits[start]]
                start += 1

            max_len = max(max_len, end - start + 1)

        return max_len
