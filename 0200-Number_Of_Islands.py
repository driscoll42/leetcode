'''
Difficulty: Medium

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
'''


class Solution:
    def explore(self, mi, ni, grid):
        if mi > 0 and grid[mi - 1][ni] == "1":
            grid[mi - 1][ni] = 0
            Solution.explore(self, mi - 1, ni, grid)
        if mi < len(grid)-1 and grid[mi + 1][ni] == "1":
            grid[mi + 1][ni] = 0
            Solution.explore(self, mi + 1, ni, grid)
        if ni > 0 and grid[mi][ni - 1] == "1":
            grid[mi][ni - 1] = 0
            Solution.explore(self, mi, ni - 1, grid)
        if ni < len(grid[0])-1 and grid[mi][ni + 1] == "1":
            grid[mi][ni + 1] = 0
            Solution.explore(self, mi, ni + 1, grid)

    def numIslands(self, grid) -> int:
        islandcnt = 0

        for mi, m in enumerate(grid):
            for ni, n in enumerate(m):
                if n == "1":
                    islandcnt += 1
                    Solution.explore("", mi, ni, grid)

        return islandcnt