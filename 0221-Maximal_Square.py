'''
Difficulty: Medium

Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
'''

from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        R = len(matrix)  # no. of rows in M[][]
        C = len(matrix[0])  # no. of columns in M[][]
        #print(R, C)

        S = [[0 for k in range(C)] for l in range(R)]
        # here we have set the first row and column of S[][]

        # Construct other entries
        for i in range(1, R):
            for j in range(1, C):
                if (matrix[i][j] == "1"):
                    S[i][j] = min(S[i][j - 1], S[i - 1][j],
                                  S[i - 1][j - 1]) + 1
                else:
                    S[i][j] = 0

        # Find the maximum entry and
        # indices of maximum entry in S[][]
        max_of_s = S[0][0]
        max_i = 0
        max_j = 0
        for i in range(R):
            for j in range(C):
                if (max_of_s < S[i][j]):
                    max_of_s = S[i][j]
                    max_i = i
                    max_j = j

        #print(max_i, max_j, max_of_s)
        return max_of_s


print(Solution.maximalSquare("", [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"],
                                  ["1", "0", "0", "1", "0"]]))
