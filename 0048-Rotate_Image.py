'''
Difficulty: Medium

You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:

Given input matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
Example 2:

Given input matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
],

rotate the input matrix in-place such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
'''
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        '''n = len(matrix) - 1
        for y in range(0, n):  # Row incrementer
            for z in range(y, (n - y)):  # Column incrementer
                temp = matrix[y][z]
                matrix[y][z] = matrix[n - z][y]
                matrix[n - z][y] = matrix[n - y][n - z]
                matrix[n - y][n - z] = matrix[z][n - y]
                matrix[z][n - y] = temp'''
        n = len(matrix[0])
        # transpose matrix
        for i in range(n):
            for j in range(i, n):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
                # reverse each row
        for i in range(n):
            matrix[i].reverse()
