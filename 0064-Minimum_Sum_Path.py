'''
Difficulty: Medium

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
'''
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # This is just a variation on Dijkstra's
        m = len(grid)
        n = len(grid[0])

        if not grid or m == 0 or n == 0:
            return 0

        # Initialize first row and column to clear things up
        for i in range(1, n):
            grid[0][i] += grid[0][i - 1]
        for i in range(1, m):
            grid[i][0] += grid[i - 1][0]


        for m in range(1, len(grid)):
            # Moves down second
            for n in range(1, len(grid[0])):
                # Moves right first
                    grid[m][n] += min(grid[m - 1][n], grid[m][n - 1])

        return grid[-1][-1]


print(Solution.minPathSum("", [[]]))
print(Solution.minPathSum("", [[1]]))
print(Solution.minPathSum("", [[1, 2]]))
print(Solution.minPathSum("", [[1], [2]]))
print(Solution.minPathSum("", [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]), Solution.minPathSum("", [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]) == 7)