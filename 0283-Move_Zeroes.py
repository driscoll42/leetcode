'''
Difficulty: Easy

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
'''
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        numzeroes = 0
        curr_nonzero = 0
        lenList = len(nums)
        for i, x in enumerate(nums):
            if x != 0:
                nums[curr_nonzero] = x
                curr_nonzero += 1
        for i, x in enumerate(nums[curr_nonzero:]):
            if x != 0:
                nums[curr_nonzero + i] = 0