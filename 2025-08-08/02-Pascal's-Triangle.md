## ✅ Problem 2: Pascal's Triangle
**Link:** [LeetCode Problem](https://leetcode.com/problems/pascals-triangle/)  
**Solution Language:** Python  
**Concepts Used:** Dynamic Programming, Combinatorics

### **Approach:**
- Used bottom-up dynamic programming to build Pascal's Triangle row by row.
- Each row starts and ends with `1`.
- Inner elements are the sum of two numbers from the previous row.
- Time complexity: **O(n²)** where `n` is the number of rows.

### **Code:**
```python
class Solution(object):
    def generate(self, numRows):
        pascal = []
        for i in range(numRows):
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = pascal[i - 1][j - 1] + pascal[i - 1][j]
            pascal.append(row)
        return pascal
```
## **Stats:**
- Runtime: 1166 ms
- Memory: 172.64 MB

