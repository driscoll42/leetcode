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
import time


class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        # This one should be closer to O(n/2**n) on average, but O(n) worst case
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

    def rangeBitwiseAnds(self, m: int, n: int) -> int:
        # Premium solution, hella efficient, I think O(log n)
        while m < n:
            print(n)
            n = n & (n - 1)
        return m & n

    def rangeBitwiseAndn(self, m: int, n: int) -> int:
        # Naive O(n) solution
        returnval = m
        if m != 0:
            for x in range(m, n + 1):
                returnval &= x
        return returnval


m = int(math.pow(2, 30))
n = 2147483647
start = time.time()
#print(Solution.rangeBitwiseAnd("", m, n))
print(time.time() - start)

start = time.time()
print(Solution.rangeBitwiseAnds("", m, n))
print(time.time() - start)

start = time.time()
#print(Solution.rangeBitwiseAndn("", m, n))
print(time.time() - start)
