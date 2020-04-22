'''
Difficulty: Medium

Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:

Input:nums = [1,1,1], k = 2
Output: 2

Note:

    The length of the array is in range [1, 20,000].
    The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].

'''
from typing import List

# TODO: Does not work, skipped to concentrate on Reinforcement Learning Final

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        start = 0
        total = 0
        cnt = 0

        for i, n in enumerate(nums):
            total += n
            while total == k:
                cnt += 1
                total -= nums[start]
                start = min(start + 1, i)

        return cnt


print(Solution.subarraySum("", [1, 1, 1], k=2))
print(Solution.subarraySum("", [1, 1, 1, 2, -2, 2], k=2))
print(Solution.subarraySum("", [1, 1, 1, 3, 5, 62, 3, 1, 1, 3, 4, -1, -1, 3, -1, -5, 7], k=2))
print(Solution.subarraySum("", [0, 0, 0, 1, 1, 1], k=2))
