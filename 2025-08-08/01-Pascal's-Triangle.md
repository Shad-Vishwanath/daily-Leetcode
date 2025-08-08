# 🧠 LeetCode Daily Practice – Day 4 (August 8, 2025)

---

## ✅ Problem 1: Soup Servings
**Link:** [LeetCode Problem](https://leetcode.com/problems/soup-servings/)  
**Solution Language:** Python  
**Concepts Used:** Recursion, Memoization, Probability

### **Approach:**
- Used recursion to simulate serving soup A and B in different quantities.
- Applied memoization (`dp`) to store already computed `(a, b)` states for efficiency.
- Base cases handle situations where one or both soups run out.
- Each state calculates probability for 4 possible serving operations.

### **Code:**
```python
class Solution:
    def f(self, a, b, dp):
        if a <= 0 and b > 0:
            return 1.0
        if a == 0 and b == 0:
            return 0.5
        if a > 0 and b <= 0:
            return 0.0
        if dp[a][b] != -1:
            return dp[a][b]

        x = 0.25 * self.f(a - 100, b, dp)
        y = 0.25 * self.f(a - 75, b - 25, dp)
        z = 0.25 * self.f(a - 50, b - 50, dp)
        w = 0.25 * self.f(a - 25, b - 75, dp)

        dp[a][b] = x + y + z + w
        return dp[a][b]
