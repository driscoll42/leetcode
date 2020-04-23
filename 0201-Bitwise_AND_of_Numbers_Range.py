'''
Difficulty: Medium

Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

Example 1:

Input: [5,7]
Output: 4

Example 2:

Input: [0,1]
Output: 0
'''
import math


class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        '''# Naive O(n) solution
        returnval = m
        if m != 0:
            for x in range(m, n + 1):
                print(x)
                returnval &= x
        return returnval'''
        # This one should be closer to O(n/2**m)
        if not m or not n or m == 0:
            return 0
        mexp = int(math.log(m, 2))
        nexp = int(math.log(n, 2))
        if mexp != nexp:
            return 0
        else:
            returnval = m
            for x in range(returnval, n + 1):
                returnval &= x
            return returnval


print(Solution.rangeBitwiseAnd("", 100, 200) == 0)
print(Solution.rangeBitwiseAnd("", 1, 2) == 0)
print(Solution.rangeBitwiseAnd("", 3, 4) == 0)
print(Solution.rangeBitwiseAnd("", 7, 8) == 0)
print(Solution.rangeBitwiseAnd("", 5, 7) == 4)
print(Solution.rangeBitwiseAnd("", 0, 1) == 0)
print(Solution.rangeBitwiseAnd("", 128, 240) == 128)
print(Solution.rangeBitwiseAnd("", 0, 4) == 0)
print(Solution.rangeBitwiseAnd("", 5, 7) == 4)
print(Solution.rangeBitwiseAnd("", 120, 127) == 120)
print(Solution.rangeBitwiseAnd("", 120, 121) == 120)
print(Solution.rangeBitwiseAnd("", 40, 58) == 32)