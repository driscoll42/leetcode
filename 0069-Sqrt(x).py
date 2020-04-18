'''
Difficulty: Easy

Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since
             the decimal part is truncated, 2 is returned.
'''
import math


class Solution:
    def mySqrt(self, x: int) -> int:
        # Slow Solution  2124 ms
        '''y = 1
        while y * y < x:
            y += 1
        if y * y > x:
            y -= 1
        return y'''

        # Newton's method   32 ms
        r = x
        while int(r * r) > x:
            r = (r + x / r) / 2
        return int(r)


for x in range(1, 20):
    print(Solution.mySqrt("", x) == int(math.sqrt(x)), x, Solution.mySqrt("", x), int(math.sqrt(x)))
