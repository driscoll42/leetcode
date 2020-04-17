'''
Difficulty: Medium

Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
'''
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lenN = len(nums)
        output = [1] * lenN
        output2 = [1] * lenN
        for i, n in enumerate(nums):
            # print(i, i+1, lenN)
            if i == lenN - 1:
                output[0] = output[lenN - 1] * n
            else:
                output[i + 1] = output[i] * n
        for i, n in enumerate(reversed(nums)):
            # print(i, i+1, lenN)
            if i == lenN - 1:
                output2[0] = output2[lenN - 1] * n
            else:
                output2[i + 1] = output2[i] * n

        # print(output)
        # print(output2)
        for i, n in enumerate(output):
            if i == 0:
                output[i] = output2[lenN - 1]
            elif i < lenN - 1:
                # print(i, n, output[i] ,output2[lenN-i-1])
                output[i] = n * output2[lenN - i - 1]
        return output