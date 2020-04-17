'''
Difficulty: Easy

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
'''
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_so_far, curr_max = nums[0], nums[0]

        if len(nums) > 1:
            for x in nums[1:]:
                curr_max = max(x, curr_max + x)
                max_so_far = max(max_so_far, curr_max)

        return max_so_far


'''
Loop for each element of the array
  (a) max_ending_here = max_ending_here + a[i]
  (b) if(max_ending_here < 0)
            max_ending_here = 0
  (c) if(max_so_far < max_ending_here)
            max_so_far = max_ending_here
return max_so_far
'''