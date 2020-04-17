'''
Difficulty: Easy

Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

After doing so, return the array.



Example 1:

Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]


Constraints:

1 <= arr.length <= 10^4
1 <= arr[i] <= 10^5
'''
from typing import List

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        currmax = 0
        for i, x in enumerate(reversed(arr)):
            if i == 0:
                currmax = x
                arr[-1] = -1
            else:
                arr[-1 - i] = currmax
                currmax = max(x, currmax)
        return arr