'''
Difficulty: Easy

Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

Example 1:
Input: [3, 2, 1]

Output: 1

Explanation: The third maximum is 1.
Example 2:
Input: [1, 2]

Output: 2

Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
Example 3:
Input: [2, 2, 3, 1]

Output: 1

Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.
'''

from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        third = None
        second = None
        one = None
        for n in nums:
            # print(n, third, second, one)
            if one is None or n > one:
                third = second
                second = one
                one = n
            elif (second is None or n > second) and n != one:
                third = second
                second = n
            elif (third is None or n > third) and n != second and n != one:
                third = n
        # print(third, second, one)
        if third is not None:
            return third
        else:
            return one

print(Solution.thirdMax("", [2, 2, 3, 1]))
'''print(Solution.thirdMax("", [1,2,-2147483648]))
print(Solution.thirdMax("", [1, 2, 2, 5, 3, 5]))
print(Solution.thirdMax("", [3, 2, 1]))
print(Solution.thirdMax("", [1, 2]))
print(Solution.thirdMax("", [2, 2, 3, 1]))'''
