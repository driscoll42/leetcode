'''
Difficulty: Medium

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
'''
from typing import List

# This could be cleaned up some, combining some of the if statements, and more efficient with the bisect command
# but the latter feels a bit like cheating in an interview, though they would probably like to see I know it

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        nums_len = len(nums)
        if nums_len == 0:
            return -1
        left, left_i = nums[0], 0
        right, right_i = nums[-1], nums_len - 1
        mid_i = nums_len // 2
        middle = nums[mid_i]

        if target == left:
            return left_i
        elif target == right:
            return right_i
        elif target == middle:
            return mid_i
        elif right_i == left_i + 1:
            return -1

        # Need to find the pivot point
        while left != right:
            # Target not found, determine if the target is in the left or right half
            if target > left and target < middle:  # split into an ascending left half with target inside
                # print(1)
                right, right_i = middle, mid_i
                mid_i = (left_i + mid_i) // 2
                middle = nums[mid_i]
            elif target > middle and target < right:  # split into an ascending right half with target inside
                # print(2)
                left, left_i = middle, mid_i
                mid_i = (right_i + mid_i) // 2
                middle = nums[mid_i]
            #  target is in the right half, along with pivot
            elif left < middle:
                # print(3)
                left, left_i = middle, mid_i
                mid_i = (right_i + mid_i) // 2
                middle = nums[mid_i]
            #  target is in the left half, along with pivot
            else:
                # print(4)
                right, right_i = middle, mid_i
                mid_i = (left_i + mid_i) // 2
                middle = nums[mid_i]

            # Check if target found
            if target == left:
                return left_i
            elif target == right:
                return right_i
            elif target == middle:
                return mid_i
            elif right_i == left_i + 1:
                return -1
        return -1

print(Solution.search("", nums=[1], target=1))
print('Should be 0')
print(Solution.search("", nums=[4, 5, 6, 7, 0, 1, 2], target=0))
print('Should be 4')
print(Solution.search("", nums=[4, 5, 6, 7, 0, 1, 2], target=3))
print('Should be -1')
print(Solution.search("", nums=[4, 5, 6, 7, 0, 1, 2, 3], target=1))
print('Should be 5')
print(Solution.search("", nums=[0, 1, 2, 3, 4, 5, 6, 7], target=1))
print('Should be 1')
print(Solution.search("", nums=[0, 1, 2, 3, 4, 5, 6, 7], target=4))
print('Should be 4')