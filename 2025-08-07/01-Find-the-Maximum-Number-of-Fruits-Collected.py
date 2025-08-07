✅ Problem 1: Find the Maximum Number of Fruits Collected
🔹 Approach: Dynamic Programming with 2-pass grid traversal
🔹 Key Idea: Track max path via adjacent cell updates using two DP arrays (prev and curr)
🔹 Time Complexity: ~O(N³) (depends on grid size and passes)
🔹 Status: Accepted
🔹 Runtime: 1894 ms
🔹 Memory: 51.57 MB (🥇 Beats 100%)

Program (Python):

class Solution(object):
    def maxCollectedFruits(self, grid):
        n = len(grid); res = 0
        for i in range(n):
            res += grid[i][i]
        for pass_ in range(2):
            if pass_ == 1:
                for i in range(n):
                    for j in range(i+1, n):
                        grid[j][i], grid[i][j] = grid[i][j], grid[j][i]
            prev = [-1] * n; prev[n - 1] = grid[0][n - 1]
            for row in range(1, n - 1):
                curr = [-1] * n
                for i in range(n):
                    if prev[i] < 0: continue
                    if i > 0: curr[i - 1] = max(curr[i - 1], prev[i] + grid[row][i - 1])
                    if i < n - 1: curr[i + 1] = max(curr[i + 1], prev[i] + grid[row][i + 1])
                    curr[i] = max(curr[i], prev[i] + grid[row][i])
                prev, curr = curr, prev
            res += prev[n - 1]
        return res
